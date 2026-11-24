# Flask CI/CD

Run the app with `python app.py` after installing `requirements.txt`.
Unit tests use the Flask test client. The integration test uses a real HTTP
request to the built app.

The staging and production jobs unpack the build, verify the HTTP endpoint
in an isolated runner, and attach the resulting package to the GitLab
deployment job. They are training deployments without a persistent server.
