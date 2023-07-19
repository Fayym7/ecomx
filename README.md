
# ECOMX

This project is like a typical Ecommerce app ,with slight upgrade in loading of several urls, this optimization is done mainly by using caching(Redis) which significantly reduce the loading time of some pages, this app has an email verification feature for User login and also this is embedded with Celery for asynchronous task distribution which in this case is the sending of email.
   This project also included a Payment gateway feature Using Paytm(Development) for secure payment.

## Getting Started

Follow these steps to run the project locally:

### Prerequisites

-Redis, Celery

### Installation

1. Clone the repository.
2. Install the required dependencies.
3. Perform any additional setup steps (e.g., database migration, configuration).

### Run the Project
1)Open an Ubuntu terminal and start a Redis server using following command:
```bash
redis-server
```                                                                                                                      
2)Once the redis server is opened ,Open another terminal a start a celery worker using this command:                                                                                                          
```bash                                                                                                                                                                                                                
celery -A ecomx worker -l info

```
3)Next, execute the following command to start the development server:   
```python

python manage.py runserver
```







