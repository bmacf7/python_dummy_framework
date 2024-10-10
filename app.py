from dummy.api import API
from dummy.middleware import Middleware

app = API()
# app.add_middleware(SomeMiddleware)

# custom middleware

class SimpleCustomMiddleware(Middleware):
    def process_request(self, req):
        print("Processing request", req.url)
    
    def process_response(self, req, resp):
        print("Processing response", req.url)

app.add_middleware(SimpleCustomMiddleware)

def custom_exception_handler(request, response, exception_cls):
    response.body = app.template("exception.html", 
                                 context={"title": "Exception Raised", 
                                          "exception": str(exception_cls)}).encode()

app.add_exception_handler(custom_exception_handler)

@app.route("/book")
class BooksResource:
    def get(self, req, resp):
        resp.text = "Books Page"
    
    def post(self, req, resp):
        resp.text = "Endpoint to create a book"

@app.route("/home") # decorator
def home(request, response):
    response.text = "Hello from the HOME page!"

@app.route("/about") # decorator
def about(request, response):
    response.text = "Hello from the ABOUT page!"

@app.route("/hello/{name}")
def greeting(request, response, name):
    response.text = f"Hello, {name}"

@app.route("/tell/{age}")
def tell_age(request, response, age):
    response.text = f"Your age is {age}"

@app.route("/sum/{num_1:d}/{num_2:d}")
def sum(request, response, num_1, num_2):
    total = int(num_1) + int(num_2)
    response.text = f"{num_1} + {num_2} = {total}"

@app.route("/template")
def template_handler(req, resp):
    resp.html = app.template("index.html", context={"title": "Lazy Framework", "name": "Lazy"})

@app.route("/exception")
def exception_throwing_handler(request, response):
    raise AssertionError("This handler should not be used.")

@app.route("/json")
def json_handler(req, resp):
    resp.json = {"name": "data", "type": "JSON"}

@app.route("/text")
def text_handler(req, resp):
    resp.text = "This is a simple text."