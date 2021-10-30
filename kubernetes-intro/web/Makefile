REGISTRY ?= "alx72n"
IMAGE ?= "web"
TAG ?= "latest"

.PHONY: build
build:
	@echo "=> build IMAGE $(REGISTRY)/$(IMAGE):$(TAG)"
	@docker build --tag $(REGISTRY)/$(IMAGE):$(TAG) .

.PHONY: build-force
build-force:
	@echo "=> build IMAGE $(REGISTRY)/$(IMAGE):$(TAG)"
	@docker build --force-rm --no-cache --tag $(REGISTRY)/$(IMAGE):$(TAG) .
