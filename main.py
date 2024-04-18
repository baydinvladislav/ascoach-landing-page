from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def get_root():
    html_content = """
    <html>
        <head>
            <title>AsCoach</title>
        </head>
        <body>
            <h1>Welcome to AsCoach</h1>
            <p>Platform where personal fitness trainers help you achieve your goals by providing personalized training plans that will make your workouts as effective as possible.</p>
            <button onclick="location.href='https://example.com/download'" type="button">Download App</button>
        </body>
    </html>
    """
    return html_content
