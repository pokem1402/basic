## Anaconda3 install

> From [Anaconda download page](https://www.anaconda.com/download/), get anaconda download file link for linux.

<pre>
  <code>
    (your shell) wget (file link)
    [example] pokem1402@~:~/Downloads$ wget https://repo.anaconda.com/archive/Anaconda3-5.2.0-Linux-x86_64.sh
  </code>
</pre>

> Downloading progress will be displayed. Then execute it

<pre>
  <code>
    (your shell) bash (file path)/(file_name).sh
    [example] pokem1402@~:~/Downloads$ bash Anaconda3-5.2.0-Linux-x86_64.sh
  </code>
</pre>

> License agreement requires your agreement. Enter 'y' to agree. To use conda easily, register path of anaconda in your bashrc.

## Check anaconda installed.

> To check anaconda installed on your machine, just enter 'conda'

<pre>
  <code>
    (your shell) conda
    [example] pokem1402@~:~/Downloads$ conda
  </code>
</pre>

> Then if it is installed well, you could see that guide for arguments of conda instructions.

## Create new virtual enviroment from Anaconda3

<pre>
  <code>
    (your shell) conda create -n (env name) python=(desired python version)
    [example] pokem1402@~:~/Download$ conda create -n my_env python=3.6
  </code>
</pre>

> Then enter 'y' to make up your own virtual enviroment.

## Activate a enviroment from Anaconda3

<pre>
  <code>
    (your shell) source activate (env name)
    [example] pokem1402@~:~/Download$ source activate my_env
  </code>
</pre>

> Then 
