odoo.define('pos_all_in_one.POSProductDetail', function(require) {
	'use strict';

	const { useExternalListener } = owl.hooks;
	const PosComponent = require('point_of_sale.PosComponent');
	const AbstractAwaitablePopup = require('point_of_sale.AbstractAwaitablePopup');
	const Registries = require('point_of_sale.Registries');
	const { useListener } = require('web.custom_hooks');
	const { useState } = owl.hooks;
	const { getDataURLFromFile } = require('web.utils');

	const rpc = require('web.rpc');
	let core = require('web.core');
	let _t = core._t;

	class POSProductDetail extends AbstractAwaitablePopup {
		constructor() {
			super(...arguments);
			this.order = arguments[1].order;
		}

		cancel() {
			this.props.resolve({ confirmed: false, payload: null });
			this.trigger('close-popup');
		}

		get imageUrl() {
            const product = this.order;
            return `/web/image?model=product.product&field=image_128&id=${product.id}&write_date=${product.write_date}&unique=1`;
        }

		async uploadImage(event) {
			const file = event.target.files[0];
			if (!file.type.match(/image.*/)) {
				await this.showPopup('ErrorPopup', {
					title: this.env._t('Unsupported File Format'),
					body: this.env._t(
						'Only web-compatible Image formats such as .png or .jpeg are supported.'
					),
				});
			} else {
				const imageUrl = await getDataURLFromFile(file);
				const loadedImage = await this._loadImage(imageUrl);
				if (loadedImage) {
					const resizedImage = await this._resizeImage(loadedImage, 800, 600);
					this.changes.image_1920 = resizedImage.toDataURL();
					// Rerender to reflect the changes in the screen
					this.render();
				}
			}
		}
		_resizeImage(img, maxwidth, maxheight) {
			var canvas = document.createElement('canvas');
			var ctx = canvas.getContext('2d');
			var ratio = 1;

			if (img.width > maxwidth) {
				ratio = maxwidth / img.width;
			}
			if (img.height * ratio > maxheight) {
				ratio = maxheight / img.height;
			}
			var width = Math.floor(img.width * ratio);
			var height = Math.floor(img.height * ratio);

			canvas.width = width;
			canvas.height = height;
			ctx.drawImage(img, 0, 0, width, height);
			return canvas;
		}
		/**
		 * Loading image is converted to a Promise to allow await when
		 * loading an image. It resolves to the loaded image if succesful,
		 * else, resolves to false.
		 *
		 * [Source](https://stackoverflow.com/questions/45788934/how-to-turn-this-callback-into-a-promise-using-async-await)
		 */
		_loadImage(url) {
			return new Promise((resolve) => {
				const img = new Image();
				img.addEventListener('load', () => resolve(img));
				img.addEventListener('error', () => {
					this.showPopup('ErrorPopup', {
						title: this.env._t('Loading Image Error'),
						body: this.env._t(
							'Encountered error when loading image. Please try again.'
						),
					});
					resolve(false);
				});
				img.src = url;
			});
		}
	

		edit_product() {
			this.showPopup('ProductDetailsEdit', {
				'product': this.order, 
			});
		}


		
	}
	
	POSProductDetail.template = 'POSProductDetail';
	Registries.Component.add(POSProductDetail);
	return POSProductDetail;
});
