## Report Generator Sample

The following sample is for running automated report generator tasks with cron jobs. 


## Test It Out

Deploy application

```
kubectl create -f ./deploy.yaml
```

Check on the status of report application(deployment,service,jobs):

```
kubectl get deployment
kubectl get jobs
kubectl get service report-view report
```

Access the report list: 

```
LB_ENDPOINT=$(kubectl get service report-view -o jsonpath="{.status.loadBalancer.ingress[*].ip}")
# Open browser with URL in MacOSX
curl http://${LB_ENDPOINT}
open http://${LB_ENDPOINT}
```

Delete application:

```
kubectl delete -f deploy.yaml
```

