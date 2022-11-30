#!/bin/bash

kubectl apply -f create_pod.yml
kubectl expose pod shop-app-pod --selector "app=shop_app" --type=LoadBalancer --port=5000
sleep 3
minikube service shop-app-pod
