import unittest
from app.main import app


class TestVideoAPI(unittest.TestCase):

    def test_health_check(self):
        """Verifica el endpoint /health."""
        with app.test_client() as client:
            response = client.get('/health')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, {'status': 'ok'})

    def test_hello(self):
        """Verifica el endpoint /."""
        with app.test_client() as client:
            response = client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, {'message': 'Bienvenido a la API de VODs!'} )

    def test_list_videos(self):
        """Verifica el endpoint /videos."""
        with app.test_client() as client:
            response = client.get('/videos')
            self.assertEqual(response.status_code, 200)
            self.assertIsInstance(response.json, list)  

    def test_get_video(self):
        """Verifica el endpoint /videos/<video_id>."""
        with app.test_client() as client:

            response = client.get('/videos/1')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json['id'], 1)
            self.assertEqual(response.json['title'], 'Película de Acción')


            response = client.get('/videos/4')
            self.assertEqual(response.status_code, 404)
            self.assertEqual(response.json, {'message': 'Video no encontrado'})


if __name__ == '__main__':
    unittest.main()
