# WrappedTFP

**WrappedTFP** is just the original [Tensorflow Projector](http://projector.tensorflow.org/) wrapped within a python _http.server_ for local use:

--------------------------------------

## Clone & Install with:
 
`pip install git+https://github.com/cedias/WrappedTFP.git`

## Usage:

Launch the projector, use `--port` to modify default port:

`python -m wrappedtpf.serve [--port 8989]`


By default it opens a new tab or browser window. If not, just navigate to `http://localhost:port`

> meant for python3.x
