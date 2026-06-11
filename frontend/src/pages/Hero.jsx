const Hero = () => {
  const scrollToProducts = () => {
    const productsSection = document.getElementById("products");
    if (productsSection) {
      productsSection.scrollIntoView({ behavior: "smooth" });
    }
  };

  return (
    <section className="hero-section py-5">
      <div className="container">
        <div className="row align-items-center">
          <div className="col-lg-6 fade-in">
            <h1 className="display-4 fw-bold mb-4">
              Discover Fresh fruits and Veggies
            </h1>
            <p className="lead mb-4">
              Find the fresh fruits and vegitables at unbeatable prices.
              Quality guaranteed with fast, secure delivery.
            </p>
            <div className="d-flex gap-3">
              <button
                type="button"
                className="btn btn-primary btn-lg"
                onClick={scrollToProducts}
              >
                <i className="bi bi-bag-plus me-2"></i>
                Shop Now
              </button>
              <button type="button" className="btn btn-outline-light btn-lg">
                <i className="bi bi-play-circle me-2"></i>
                Learn More
              </button>
            </div>
          </div>
          <div className="col-lg-6 text-center">
            <img
              src="https://www.rush.edu/sites/default/files/2020-10/colorful-fruits-vegetables-og.jpg"
              alt="Fruits and Veggies"
              className="img-fluid rounded-3 shadow-lg"
              style={{ maxHeight: "400px", objectFit: "cover" }}
            />
          </div>
        </div>
      </div>
    </section>
  );
};

export default Hero;
