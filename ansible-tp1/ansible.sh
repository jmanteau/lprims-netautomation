#ansible-playbook -i inventory.txt playbook-apply.yml -v

#IMAGE=willhallonline/ansible
IMAGE=ansible-docker:latest
docker run --rm -it -v $(pwd):/ansible --workdir=/ansible $IMAGE ansible-playbook -i inventory.txt playbook-apply.yml -vvv
