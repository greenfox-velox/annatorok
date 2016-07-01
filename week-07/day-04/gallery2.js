'use strict';

var images = [
  {
    number: 'Image 1',
    path: 'images/photoMain.jpg',
  },
  {
    number: 'Image 1',
    path: 'images/photo1.jpg',
  },
  {
    number: 'Image 2',
    path: 'images/photo2.jpg',
  },
  {
    number: 'Image 3',
    path: 'images/photo3.jpg',
  },
  {
    number: 'Image 4',
    path: 'images/photo4.jpg',
  },
  {
    number: 'Image 5',
    path: 'images/photo5.jpg',
  },
  {
    number: 'Image 6',
    path: 'images/photo6.jpg',
  },
  {
    number: 'Image 7',
    path: 'images/photo7.jpg',
  },
  {
    number: 'Image 8',
    path: 'images/photo8.jpg',
  },
];

// create and insert main image
var currentImage = 0;
var mainPictureContainer = document.querySelector('.main-picture-container');
var picture = document.createElement('img');
picture.setAttribute('src', images[0].path);
mainPictureContainer.appendChild(picture);

// create and insert thumbnail images
var thumbnailDiv = document.querySelector('.thumbnails-gallery');
var number = document.querySelector('p');
images.forEach(function (e) {
  var thumbnailImages = document.createElement('img');
  thumbnailImages.setAttribute('src', e.path);
  thumbnailDiv.appendChild(thumbnailImages);
  // add click function to thumbnail images
  thumbnailImages.addEventListener('click', function () {
    picture.setAttribute('src', e.path);
    number.textContent = e.number;
  });
});

// switch main image with other images in the gallery list
function getNewPic() {
  var mainImage = document.querySelector('.main-picture-container img');
  mainImage.setAttribute('src', images[currentImage].path);
  number.textContent = images[currentImage].number;
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

// thumbnail
var thumbImage = 0;
function slide() {
  for (var i = thumbImage; i < thumbImage + 4; i++) {
    var thumbnailImages = document.createElement('img');
    thumbnailImages.setAttribute('src', images[i].path);
    thumbnailDiv.appendChild(thumbnailImages);
    addtoThumbnails(i, thumbnailImages);
  }
}

function addtoThumbnails(i, thumbnailImages) {
  thumbnailImages.addEventListener('click', function () {
    picture.setAttribute('src', images[i].path);
    number.textContent = images[i].number;
  });
}


// // cycle through the thumbnail images, index increse/decrease
function nextThumb() {
  if (thumbImage + 4 < images.length - 1) {
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
