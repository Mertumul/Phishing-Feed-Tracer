from fastapi import FastAPI
from setup import SessionLocal, Phishing
import uvicorn

app = FastAPI()

with SessionLocal() as session:

    @app.get("/phishing/scan")
    def get_phishing_sites():
        """
        Endpoint to get all phishing feeds from the database.

        Args:
            None.

        Returns:
            dict: A dictionary containing a list of phishing site URLs.
        """

        phishing_sites = session.query(Phishing).all()
        return {"phishing_sites": [site.url for site in phishing_sites]}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
