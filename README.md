# platformsh-client-python


### Installation

```
python setup.py install
```

### Usage

Set the `$PLATFORMSH_API_TOKEN` environment variable and then make calls to the endpoints.


### Endpoints

Currently only:

- subscriptions
- environments


## Example

```python
import pshclient
PROJECT_ID = 'your_project_id'
PROJECT_ID = 'some_environment'

data = pshclient.environments(PROJECT_ID, ENVIRONMENT)
```
