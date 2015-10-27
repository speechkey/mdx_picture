mdx_picture: HTML 5.1 <picture> for Markdown
============================================

[![Build Status](https://travis-ci.org/speechkey/mdx_picture.svg)](https://travis-ci.org/speechkey/mdx_picture)

## Abstract

The HTML `<picture>` element is a container used to specify multiple `<source>`s for a specific `<img>`. The browser will choose the most suitable source according to the current layout of the page and the screen it will be displayed on:

```html
<picture>
	<source srcset="pear-mobile.jpeg" media="(max-width: 720px)">
	<source srcset="pear-tablet.jpeg" media="(max-width: 1280px)">
	<source srcset="pear-desktop.jpeg">
	<img src="pear-tablet.jpeg" alt="The pear is juicy.">
</picture>
```

The `<picture>` was introduced in the [HTML 5.1 draft](http://www.w3.org/html/wg/drafts/html/master/semantics.html#the-picture-element) and implemented only in [most current browsers Firefox > 38, Chrome > 43](http://caniuse.com/#feat=picture). The lack of support of the tag by IE and Safari makes it imposible to use the plain `<picture>` element. Fortunately there is a plenty of polyfills which enables `<picture>` element in browsers without its support.

## Objective

Implement a markdown extension with a markup for `<picture>` tag. **Attention! The `mdx_picture` doesn't implement any polyfills, so it supports only browsers with native `<picture>` tag support. You should add a polyfill implementation by yourself.**

## Use

The markdown block

```markdown
[picture]
	[720px]: pear-mobile.jpeg
	[1280px]: pear-tablet.jpeg
	![This picture loads on non-supporting browsers.](image.jpg "The image title")
[/picture]
```
gets converted to

```html
<picture>
	<source srcset="pear-mobile.jpeg" media="(max-width: 720px)">
	<source srcset="pear-tablet.jpeg" media="(max-width: 1280px)">
	<img alt="This picture loads on non-supporting browsers." src="image.jpg" title="The image title" />
</picture>
```

## Install

- From PyPi `pip install mdx_picture`
- From Github `pip install git+git://github.com/speechkey/mdx_picture`

## Develop

1. Create new virtual environment e.g. `mkvirtualenv mdx_picture`
2. Install dependencies by `pip install -r requirements.pip`

## Test

Test extension by `python setup.py test`