# Sample API made with Falcon

Sample application that illustrates the minimal use of the Falcon framework and external API consumption.

### Requirements

-   Python 3.9.0 (installation via pyenv recommended)
-   Pipenv (installation with brew recommended)

### Installation

Once you satisfy the requirements, go to the project folder and run:

```
pipenv install --dev
```

### Running the project

To serve the API enter:

```
pipenv run start
```

Once running try hitting a couple of paths such as:

```
curl -v http://127.0.0.1:8000/
curl -v http://127.0.0.1:8000/weather/mex
curl -v http://127.0.0.1:8000/weather/san%20fran
```

_Note: the external weather API is very limited in terms of cities it can provide, try mostly USA cities._

### Testing

Testing is done with pytest, just run:

```
pipenv run test
```

### Resources

-   [Falcon - Web framework](https://github.com/falconry/falcon)
-   [Pyenv - Python version management](https://github.com/pyenv/pyenv)
-   [Pipenv - Python development workflow](https://github.com/pypa/pipenv)
-   [Pytest - Testing framework](https://github.com/pytest-dev/pytest/)
