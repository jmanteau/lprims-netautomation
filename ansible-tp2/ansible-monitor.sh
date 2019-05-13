#ansible-playbook -i inventory.txt playbook-monitor.yml -v

IMAGE=ansible-docker:latest
docker run --rm -it -v $(pwd):/ansible --workdir=/ansible $IMAGE ansible-playbook -i inventory.txt playbook-monitor.yml
