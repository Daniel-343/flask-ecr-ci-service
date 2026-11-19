# flask-ecr-ci-service

Small Flask app for the CSK week 10 CI/CD workshop. `GET /` returns a greeting on port 8080.

## Running it

```bash
uv run python -m unittest -v
uv run app.py          # curl localhost:8080

docker build -t hello .
docker run -p 8080:8080 hello
```

## CI

- PRs to main run the tests and build the image (no push).
- Pushes to main run the tests, then build and push to ECR. Needs the `AWS_ROLE_ARN`, `AWS_REGION` and `ECR_REPOSITORY_URL` repo variables.

The image tag is the version in pyproject.toml, it needs to be updated manually.

```bash
uv version --bump minor
```
