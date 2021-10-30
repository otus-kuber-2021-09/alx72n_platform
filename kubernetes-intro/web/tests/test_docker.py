from expects import equal
from expects import expect
from expects import contain
from pytest import mark
from testinfra.host import Host
import requests
from requests import Response


@mark.describe("image")
def test_build_docker_image_finishes_successfully(
    host: Host,
) -> None:
    expect(host.run("make build").rc).to(equal(0))


@mark.describe("image")
def test_docker_image_exists_in_registry(
    host: Host,
) -> None:
    expect(host.run("docker pull alx72n/web:latest").rc).to(equal(0))


def stop_web_container(host: Host) -> None:
    rc_code: int = host.run("docker rm --force web").rc
    if rc_code != 0:
        exit(1)


def start_web_container(host: Host):
    rc_code: int = host.run(
        "docker run --detach --rm --publish 8000:8000 --volume"
        " $(pwd)/tests/homework.html:/app/homework.html --name web alx72n/web:latest"
    ).rc
    if rc_code != 0:
        exit(1)


@mark.describe("web")
def test_web_server_is_starting(
    host: Host,
) -> None:
    stop_web_container(host)
    start_web_container(host)
    expect(host.docker("web").is_running).to(equal(True))
    stop_web_container(host)


@mark.describe("web")
def test_web_server_returns_page_from_app_directory(
    host: Host,
) -> None:
    start_web_container(host)
    response: Response = requests.get(
        url="http://localhost:8000/homework.html"
    )
    expect(response.text).to(contain("Hello, World!"))
    stop_web_container(host)
