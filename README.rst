Digital image steganography of encrypted text
========================================================================
JPG, GIF, PNG, BMP.

日本語ドキュメント: `Japanese Document`_


Installation
-----------------

.. code-block:: bash

    $ pip install steganography


Example Image
-----------------

.. image:: http://subc.github.io/image/pypi/steganography.png
    :alt: HTTPie compared to cURL
    :align: center


Sample Command
-----------------

.. code-block:: bash

    # encode example: hide text to image
    >>>steganography -e /tmp/image/input.jpg /tmp/image/output.jpg 'The quick brown fox jumps over the lazy dog.'

    # decode example: read secret text from image
    >>>steganography -d /tmp/image/output.jpg
    The quick brown fox jumps over the lazy dog.

Sample Code
-----------------

.. code-block:: python

    # -*- coding: utf-8 -*-
    from __future__ import absolute_import, unicode_literals
    from steganography.steganography import Steganography

    # hide text to image
    path = "/tmp/image/input.jpg"
    output_path = "/tmp/image/output.jpg"
    text = 'The quick brown fox jumps over the lazy dog.'
    Steganography.encode(path, output_path, text)

    # read secret text from image
    secret_text = Steganography.decode(output_path)

Documentation
-----------------

- 日本語ドキュメント: `Japanese Document`_

.. _`Japanese Document`: http://qiita.com/haminiku/items/2e623caab751f25a382e
