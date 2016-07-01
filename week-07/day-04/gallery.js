'use strict';

var images = [
  {
    title: 'Main Image',
    path: 'images/photoMain.jpg',
  },
  {
    title: 'Image 1',
    path: 'images/photo1.jpg',
  },
  {
    title: 'Image 2',
    path: 'images/photo2.jpg',
  },
  {
    title: 'Image 3',
    path: 'images/photo3.jpg',
  },
  {
    title: 'Image 4',
    path: 'images/photo4.jpg',
  },
  {
    title: 'Image 5',
    path: 'images/photo5.jpg',
  },
  {
    title: 'Image 6',
    path: 'images/photo6.jpg',
  },
  {
    title: 'Image 7',
    path: 'images/photo7.jpg',
  },
  {
    title: 'Image 8',
    path: 'images/photo8.jpg',
  },
];

// create and insert main image
var mainPictureContainer = document.querySelector('.main-picture-container');
var picture = document.createElement('img');
picture.setAttribute('src', 'images/photoMain.jpg');
mainPictureContainer.appendChild(picture);

// switch main image with other images in the gallery list
var currentImage = 0;
function getNewPic() {
  var mainImage = document.querySelector('.main-picture-container img');
  mainImage.setAttribute('src', images[currentImage].path);
  title.textContent = images[currentImage].title;
}

// cycle through the main images, index increse/decrease
function nextImage() {
  if (currentImage < images.length - 1) {
    currentImage++;
  } else {
    currentImage = 0;
  }
}

function prevImage() {
  if (currentImage > 0) {
    currentImage--;
  } else {
    currentImage = images.length - 1;
  }
}

// add click events to main next & prev buttons
var next = document.querySelector('.main-next-bt');
next.addEventListener('click', function() {
  nextImage();
  getNewPic();
});

var prev = document.querySelector('.main-prev-bt');
prev.addEventListener('click', function () {
  prevImage();
  getNewPic();
});

// create and insert thumbnail images
var thumbnailDiv = document.querySelector('.thumbnails-gallery');
var title = document.querySelector('p');

images.forEach(function (e) {
  var thumbnailImages = document.createElement('img');
  thumbnailImages.setAttribute('src', e.path);
  thumbnailDiv.appendChild(thumbnailImages);
  // add click function to thumbnail images
  thumbnailImages.addEventListener('click', function () {
    picture.setAttribute('src', e.path);
    title.textContent = e.title;
  });
});

function addtoThumbnails(i, thumbnailImages) {
  thumbnailImages.addEventListener('click', function () {
    picture.setAttribute('src', images[i].path);
    title.textContent = images[i].title;
  });
}

// thumbnail slide through images
var thumbImage = 0;
function slide() {
  for (var i = thumbImage; i < thumbImage + 4; i++) {
    var thumbnailImages = document.createElement('img');
    thumbnailImages.setAttribute('src', images[i].path);
    thumbnailDiv.appendChild(thumbnailImages);
    addtoThumbnails(i, thumbnailImages);
  }
}

// // cycle through the thumbnail images, index increse/decrease
function nextThumb() {
  if (thumbImage + 4 < images.length) {
    thumbImage++;
  }
}

function prevThumb() {
  if (thumbImage > 0) {
    thumbImage--;
  }
}

// add click events to thumbnail next & prev buttons
var thumbNext = document.querySelector('.thumb-next-bt');
thumbNext.addEventListener('click', function () {
  thumbnailDiv.innerHTML = '';
  nextThumb();
  slide();
});

var thumbPrev = document.querySelector('.thumb-prev-bt');
thumbPrev.addEventListener('click', function () {
  thumbnailDiv.innerHTML = '';
  prevThumb();
  slide();;
});
