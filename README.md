# Taskiq with aiogram 3 example

This is an example of using Taskiq together with the aiogram framework for heavy background and delayed tasks.

### Used technology
* Python 3.12;
* aiogram 3.x (Asynchronous Telegram Bot framework);
* dynaconf (Configuration Management for Python);
* taskiq (Async Distributed Task Manager);
* Docker and Docker Compose (containerization);
* NATS (queue);
* Redis (tasks source).

## Installation

1. Clone the repository to your local machine via HTTPS:

```bash
git clone https://github.com/kmsint/taskiq_example.git
```
or via SSH:
```bash
git clone git@github.com:kmsint/taskiq_example.git
```

2. Create a `docker-compose.yml` file in the root of the project and copy the code from the `docker-compose.example` file into it.

3. Create a `.env` file in the root of the project and copy the code from the `.env.example` file into it. Replace the required secrets (BOT_TOKEN).

4. Run `docker-compose.yml` with `docker compose up` command. You need docker and docker-compose installed on your local machine.

5. Create a virtual environment in the project root and activate it.

6. Install the required libraries in the virtual environment. With `pip`:
```bash
pip install .
```
or if you use `poetry`:
```bash
poetry install
```
7. Start the taskiq worker with command:
```bash
taskiq worker app.infrastructure.scheduler.taskiq_broker:broker -fsd
```
and then start the scheduler:
```bash
taskiq scheduler app.infrastructure.scheduler.taskiq_broker:scheduler -fsd
```
8. Run `__main__.py` to check the functionality of the example.