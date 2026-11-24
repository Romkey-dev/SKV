# Git Hooks and CI

[![pipeline status](https://gitlab.com/Romkey-dev/hooks-lab5/badges/main/pipeline.svg)](https://gitlab.com/Romkey-dev/hooks-lab5/-/pipelines)

Install the repository hooks with `bash install-hooks.sh`. Run the tests with
`python3 -m unittest -v`.

The manual deploy publishes a versioned archive as a job artifact. Set the
CI/CD variable `APP_VERSION` to override the YAML default. To push a release
tag, configure a masked, protected `RELEASE_TOKEN` with repository write
access and permission to create the corresponding tag.
