# jarvis

Jarvis (the abbreviations of Just A Rather Very Intelligent System) is
a digital butler. He can read PDF files and sum.

Specification
----------
LLM: [llama3](https://www.llama.com/models/llama-3/)

Embedding: Ollama, [nomic-embed-text](https://ollama.com/library/nomic-embed-text)

Usage
----------
1. Get source code
``` console
$ git clone https://github.com/manbing/jarvis.git
```

2. Enter directory
``` console
$ cd jarvis 
```

3. Run program. 
``` console
$ python jarvis.py
```
Process will read all PDF files under the directory, `~/Documentation`.

It had a PDF file, [lkmpg.pdf](https://github.com/sysprog21/lkmpg), already.

3. Ask question about lkmpg.pdf
``` console
Q: What is kernel module?
```

4. Get reply
``` console
Jarvis: A kernel module is precisely defined as a code segment capable of
dynamic loading and unloading within the kernel as needed. These modules
enhance kernel capabilities without necessitating a system reboot.
```

TODO
----------
* Reading the diagram, table and so on, in PDF file
* Listening
* Speaking

Reference
----------
[lkmpg](https://github.com/sysprog21/lkmpg)
