# tested with python2.7 and 3.4
from spyre import server

from skimage import data


class ImageEditor(server.App):
    title = "Image Editor"
    inputs = [
        {
            "type": "slider",
            "key": "sigma",
            "label": "sigma",
            "value": 0.1, "max": 10, "step": 0.1,
            "action_id": "image"},
        {
            "type": "slider",
            "key": "red",
            "label": "red",
            "value": 1, "max": 1, "step": 0.1,
            "action_id": "image"},
        {
            "type": "slider",
            "key": "green",
            "label": "green",
            "value": 1, "max": 1, "step": 0.1,
            "action_id": "image"},
        {
            "type": "slider",
            "key": "blue",
            "label": "blue",
            "value": 1, "max": 1, "step": 0.1,
            "action_id": "image"
        }
    ]

    controls = [{
        "type": "hidden",
        "id": "render",
        "label": "render"
    }]

    outputs = [{
        "type": "image",
        "id": "image",
        "control_id": "render"
    }]

    def getImage(self, params):
        sigma = float(params['sigma'])
        r = float(params['red'])
        g = float(params['green'])
        b = float(params['blue'])
        image = data.coffee()
        new_image = filter.gaussian_filter(image, sigma=sigma, multichannel=True)
        new_image[:, :, 0] = r * new_image[:, :, 0]
        new_image[:, :, 1] = g * new_image[:, :, 1]
        new_image[:, :, 2] = b * new_image[:, :, 2]
        return new_image


if __name__ == '__main__':
    app = ImageEditor()
    app.launch(port=9096)