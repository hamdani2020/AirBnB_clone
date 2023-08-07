# 0x00. AirBnB clone - The console
## Welcome to the AirBnB clone project!

## Authors/ Collaborators
- [Alhassan Hamdani Gandi](www.github.com/hamdani2020)
- [Eric Kwakye Boateng](www.github.com/erickwakyeboateng)

## Resources Needed
Read or watch
- [cmd module](https://docs.python.org/3.8/library/cmd.html)
- [comd module in depth](http://pymotw.com/2/cmd/)
- [uuid module](https://docs.python.org/3.8/library/uuid.html)
- [datetime](https://docs.python.org/3.8/library/datetime.html)
- [unittest modules](https://docs.python.org/3.8/library/unittest.html#module-unittest)
- [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
- [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)
- [cmd module wiki page](https://wiki.python.org/moin/CmdModule)
- [python unittest](https://realpython.com/python-testing/)

## Project Execution Workflow
How your shell should work
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

But in non-interactive mode: (like the Shell project in C)

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

All test should also pass in non-interactive mode: ``$ echo "python3 -m unittest discover tests" | bash``


[![Flowchart](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230807%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230807T120545Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=9e4adfd2d2e0f3777c1f1449305674b82596e70586ce9bb7e6302679652f60e6)
