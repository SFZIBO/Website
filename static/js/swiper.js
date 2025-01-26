const categoryCarousel = new Swiper('.category-carousel', {
    slidesPerView: 6, // Menampilkan 6 gambar per layar
    spaceBetween: 20,
    navigation: {
      nextEl: '.category-carousel-next',
      prevEl: '.category-carousel-prev',
    },
  });

  const productsCarousel = new Swiper('.swiper', {
    slidesPerView: 6, // Menampilkan 6 gambar per layar
    spaceBetween: 20,
    navigation: {
      nextEl: '.products-carousel-next',
      prevEl: '.products-carousel-prev',
    },
  });
  