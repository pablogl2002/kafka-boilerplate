# kafka-python-boilerplate

### Dependencies
1. Create a virtual environemtn to run the docker compose file
2. ```pip install -r requirements.txt```
3. Run the docker compaoe file first ```docker-compose up -d```
4. Step3 will create a docker image and this shall look as below
```
[+] Running 7/0
 ⠿ Container zk               Running                                                                               0.0s
 ⠿ Container cli-tools        Running                                                                               0.0s
 ⠿ Container broker2          Running                                                                               0.0s
 ⠿ Container broker0          Running                                                                               0.0s
 ⠿ Container broker1          Running                                                                               0.0s
 ⠿ Container schema-registry  Running                                                                               0.0s
 ⠿ Container kafka-connect    Running                                             
```

5. Now run the main.py file : ```faust -A main worker -l info```
The above command will make the worker ready. 

6. This is the way to manually test it ( This is only for agents demo app testing)
```
(1) To test open a new terminal and enter to virtaul env and execute 'docker exec -it cli-tools kafka-topics --list --bootstrap-server broker0:29092'
__consumer_offsets
_connect-configs
_connect-offsets
_connect-status
_schemas
greetings
[2023-02-07 14:20:18,274] [71696] [INFO] [^---Fetcher]: Starting... 
[2023-02-07 14:20:18,275] [71696] [INFO] [^---Recovery]: Worker ready 
[2023-02-07 14:20:18,276] [71696] [INFO] [^Worker]: Ready 
[2023-02-07 14:23:42,617] [71696] [WARNING] Greeting is 'hello stream processor ' 
[2023-02-07 14:24:05,728] [71696] [WARNING] Greeting is 'hello again' 


(2) docker exec -it cli-tools kafka-console-producer --topic greetings --bootstrap-server broker0:29092
>hello stream processor 
>hello again
```
