from django.test import TestCase, Client

# Create your tests here.

class mainTest(TestCase):
    #Test untuk mengecek apakah web bisa ditampilkan jika tidak ada /main/
    def test_url_without_main(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)
    
    #Test untuk mengecek apakah web bisa ditampilkan jika ada /main/
    def test_url_with_main(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)
    
    #Test untuk mengecek apakah web gagal ditampilkan jika diluar /main/ dan path kosong
    def test_error_url(self):
        response = Client().get('/error/')
        self.assertEqual(response.status_code, 404)

    #Test untuk mengecek apakah web menggunakan template dari main.html
    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')