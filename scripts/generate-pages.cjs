const fs = require('fs');
const path = require('path');

const eventHtml = fs.readFileSync('public/event.html', 'utf8');

const headerEndMarker = '<!-- end of header -->';
const footerStartMarker = '<!-- start of footer-section -->';

const headerIdx = eventHtml.indexOf(headerEndMarker);
const footerIdx = eventHtml.indexOf(footerStartMarker);

if (headerIdx === -1 || footerIdx === -1) {
  console.error('Could not find header or footer markers');
  process.exit(1);
}

const headerPart = eventHtml.substring(0, headerIdx + headerEndMarker.length);
const footerPart = eventHtml.substring(footerIdx);

function createPage(title, description, breadcrumbTitle, contentHtml) {
  // customize title and meta in header
  let pageHeader = headerPart.replace(
    /<title>.*?<\/title>/,
    `<title>${title} | Quran Teacher - Istiqbal Islamic Centre</title>\n    <meta name="description" content="${description}">\n    <meta property="og:title" content="${title} | Quran Teacher - Istiqbal Islamic Centre">\n    <meta property="og:description" content="${description}">`
  );

  const breadcrumbHtml = `
        <!-- start of breadcumb -->
        <div class="wpo-breadcumb-area">
            <div class="container">
                <div class="row">
                    <div class="col-12">
                        <div class="wpo-breadcumb-wrap">
                            <h2>${breadcrumbTitle}</h2>
                            <ul>
                                <li><a href="index.html">Home</a></li>
                                <li><span>${breadcrumbTitle}</span></li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- end of breadcumb -->
`;

  return `${pageHeader}
${breadcrumbHtml}
${contentHtml}
${footerPart}`;
}

// 1. ABOUT PAGE
const aboutContent = `
        <!-- start of wpo-about-section -->
        <section class="wpo-about-section section-padding">
            <div class="container">
                <div class="row align-items-center">
                    <div class="col-lg-6 col-md-12 col-12">
                        <div class="wpo-about-wrap">
                            <div class="wpo-about-img">
                                <img src="assets/images/page-title.jpg" alt="About Istiqbal" style="border-radius: 8px; width: 100%; object-fit: cover; max-height: 450px;">
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-6 col-md-12 col-12">
                        <div class="wpo-about-text">
                            <div class="wpo-section-title">
                                <span>About Istiqbal Centre</span>
                                <h2>Seeking Knowledge &amp; Building a Faithful Community</h2>
                            </div>
                            <p>Istiqbal Islamic Centre &amp; Quran Teacher academy provides authentic Islamic education, Quran recitation with Tajweed, Hifz programs, and community support for Muslims worldwide. Founded on the principles of the Quran and Sunnah, our mission is to nurture strong moral character and spiritual growth.</p>
                            <p>We welcome learners of all ages, from young children taking their first steps in Noorani Qaida to adults seeking in-depth understanding of Islamic sciences.</p>
                            <div class="btns" style="margin-top: 25px;">
                                <a href="service.html" class="theme-btn">Our Services</a>
                                <a href="contact.html" class="theme-btn s2" style="margin-left: 15px;">Contact Us</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- start of pillars section -->
        <section class="wpo-pillars-section section-padding" style="background: #fbfbfb; padding: 70px 0;">
            <div class="container">
                <div class="row">
                    <div class="col-12 text-center">
                        <div class="wpo-section-title">
                            <span>The Foundations of Islam</span>
                            <h2>The 5 Pillars of Islam</h2>
                        </div>
                    </div>
                </div>
                <div class="row" style="margin-top: 30px;">
                    <div class="col-lg-2 col-md-4 col-sm-6 col-12 offset-lg-1 mb-4 text-center">
                        <div style="background: #fff; padding: 25px 15px; border-radius: 6px; box-shadow: 0 4px 15px rgba(0,0,0,0.06); height: 100%;">
                            <i class="fi flaticon-quran" style="font-size: 38px; color: #DB9E30;"></i>
                            <h4 style="margin-top: 15px; font-size: 18px; font-weight: 700;">Shahadah</h4>
                            <p style="font-size: 13px; color: #777;">Declaration of Faith in Allah and His Messenger.</p>
                        </div>
                    </div>
                    <div class="col-lg-2 col-md-4 col-sm-6 col-12 mb-4 text-center">
                        <div style="background: #fff; padding: 25px 15px; border-radius: 6px; box-shadow: 0 4px 15px rgba(0,0,0,0.06); height: 100%;">
                            <i class="fi flaticon-prayer" style="font-size: 38px; color: #DB9E30;"></i>
                            <h4 style="margin-top: 15px; font-size: 18px; font-weight: 700;">Salah</h4>
                            <p style="font-size: 13px; color: #777;">Performing the five daily obligatory prayers.</p>
                        </div>
                    </div>
                    <div class="col-lg-2 col-md-4 col-sm-6 col-12 mb-4 text-center">
                        <div style="background: #fff; padding: 25px 15px; border-radius: 6px; box-shadow: 0 4px 15px rgba(0,0,0,0.06); height: 100%;">
                            <i class="fi flaticon-ramadan" style="font-size: 38px; color: #DB9E30;"></i>
                            <h4 style="margin-top: 15px; font-size: 18px; font-weight: 700;">Sawm</h4>
                            <p style="font-size: 13px; color: #777;">Fasting during the holy month of Ramadan.</p>
                        </div>
                    </div>
                    <div class="col-lg-2 col-md-4 col-sm-6 col-12 mb-4 text-center">
                        <div style="background: #fff; padding: 25px 15px; border-radius: 6px; box-shadow: 0 4px 15px rgba(0,0,0,0.06); height: 100%;">
                            <i class="fi flaticon-charity" style="font-size: 38px; color: #DB9E30;"></i>
                            <h4 style="margin-top: 15px; font-size: 18px; font-weight: 700;">Zakat</h4>
                            <p style="font-size: 13px; color: #777;">Purifying wealth by giving to those in need.</p>
                        </div>
                    </div>
                    <div class="col-lg-2 col-md-4 col-sm-6 col-12 mb-4 text-center">
                        <div style="background: #fff; padding: 25px 15px; border-radius: 6px; box-shadow: 0 4px 15px rgba(0,0,0,0.06); height: 100%;">
                            <i class="fi flaticon-kaaba" style="font-size: 38px; color: #DB9E30;"></i>
                            <h4 style="margin-top: 15px; font-size: 18px; font-weight: 700;">Hajj</h4>
                            <p style="font-size: 13px; color: #777;">Pilgrimage to Makkah once in a lifetime if able.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
`;

// 2. CONTACT PAGE
const contactContent = `
        <!-- start of wpo-contact-pg-section -->
        <section class="wpo-contact-pg-section section-padding">
            <div class="container">
                <div class="row">
                    <div class="col col-lg-10 offset-lg-1">
                        <div class="office-info">
                            <div class="row">
                                <div class="col col-xl-4 col-lg-6 col-md-6 col-12">
                                    <div class="office-info-item">
                                        <div class="office-info-icon">
                                            <div class="icon">
                                                <i class="fi flaticon-placeholder"></i>
                                            </div>
                                        </div>
                                        <div class="office-info-text">
                                            <h2>Address</h2>
                                            <p>7 Green Lake Street Crawfordsville, IN 47933</p>
                                        </div>
                                    </div>
                                </div>
                                <div class="col col-xl-4 col-lg-6 col-md-6 col-12">
                                    <div class="office-info-item">
                                        <div class="office-info-icon">
                                            <div class="icon">
                                                <i class="fi flaticon-email"></i>
                                            </div>
                                        </div>
                                        <div class="office-info-text">
                                            <h2>Email Us</h2>
                                            <p>istiqbal@gmail.com</p>
                                            <p>info@istiqbal.org</p>
                                        </div>
                                    </div>
                                </div>
                                <div class="col col-xl-4 col-lg-6 col-md-6 col-12">
                                    <div class="office-info-item">
                                        <div class="office-info-icon">
                                            <div class="icon">
                                                <i class="fi flaticon-phone-call"></i>
                                            </div>
                                        </div>
                                        <div class="office-info-text">
                                            <h2>Call Now</h2>
                                            <p>+1 800 123 456 789</p>
                                            <p>+1 800 987 654 321</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="wpo-contact-title">
                            <h2>Have Any Question?</h2>
                            <p>Feel free to reach out to our team regarding Quran classes, prayer timings, donations, or community programs.</p>
                        </div>
                        <div class="wpo-contact-form-area">
                            <form method="post" id="contact-form-main" onsubmit="event.preventDefault(); document.getElementById('success').style.display='block';">
                                <div>
                                    <input type="text" class="form-control" name="name" id="name" placeholder="Your Name*" required>
                                </div>
                                <div>
                                    <input type="email" class="form-control" name="email" id="email" placeholder="Your Email*" required>
                                </div>
                                <div>
                                    <input type="text" class="form-control" name="phone" id="phone" placeholder="Your Phone*">
                                </div>
                                <div>
                                    <select name="subject" class="form-control">
                                        <option disabled="disabled" selected="">Select Service</option>
                                        <option>Quran Teaching (Tajweed)</option>
                                        <option>Hifz Program</option>
                                        <option>Islamic Studies for Kids</option>
                                        <option>Mosque Visit / Tour</option>
                                        <option>Donation &amp; Zakat Inquiries</option>
                                    </select>
                                </div>
                                <div class="fullwidth">
                                    <textarea class="form-control" name="note" id="note" placeholder="Message..." required></textarea>
                                </div>
                                <div class="submit-area">
                                    <button type="submit" class="theme-btn">Get in Touch</button>
                                </div>
                                <div class="clearfix error-handling-messages" style="margin-top: 15px;">
                                    <div id="success" style="display:none; color: green; font-weight: 600;">JazakAllah Khair! Your message has been sent successfully. We will contact you soon.</div>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
            <section class="wpo-contact-map-section" style="margin-top: 60px;">
                <div class="wpo-contact-map">
                    <iframe src="https://maps.google.com/maps?q=Crawfordsville%20IN&t=&z=13&ie=UTF8&iwloc=&output=embed" style="border:0; width:100%; height:450px;" allowfullscreen="" loading="lazy"></iframe>
                </div>
            </section>
        </section>
`;

// 3. DONATE PAGE
const donateContent = `
        <!-- start of wpo-donation-section -->
        <section class="wpo-donation-section section-padding">
            <div class="container">
                <div class="row">
                    <div class="col-lg-8 offset-lg-2">
                        <div class="wpo-donate-header">
                            <h2>Support Istiqbal Islamic Centre</h2>
                            <p style="margin-top: 10px; color: #666;">"The believer's shade on the Day of Resurrection will be their charity." (Tirmidhi)</p>
                        </div>
                        <form action="#" method="post" id="donation-form" onsubmit="event.preventDefault(); document.getElementById('donate-success').style.display='block';">
                            <div class="wpo-donations-amount">
                                <h2>1. Choose Donation Amount</h2>
                                <div class="amount-btn-wrapper" style="display: flex; gap: 10px; flex-wrap: wrap; margin-bottom: 20px;">
                                    <button type="button" class="theme-btn s2 amount-btn" onclick="document.getElementById('custom-amount').value='20';">$20</button>
                                    <button type="button" class="theme-btn s2 amount-btn" onclick="document.getElementById('custom-amount').value='50';">$50</button>
                                    <button type="button" class="theme-btn amount-btn" onclick="document.getElementById('custom-amount').value='100';">$100</button>
                                    <button type="button" class="theme-btn s2 amount-btn" onclick="document.getElementById('custom-amount').value='250';">$250</button>
                                    <button type="button" class="theme-btn s2 amount-btn" onclick="document.getElementById('custom-amount').value='500';">$500</button>
                                </div>
                                <div class="form-group">
                                    <label style="font-weight: 600; margin-bottom: 8px;">Or Enter Custom Amount ($ USD):</label>
                                    <input type="number" id="custom-amount" class="form-control" value="100" min="5" step="1" required>
                                </div>
                            </div>
                            <div class="wpo-donations-details">
                                <h2>2. Donation Cause &amp; Details</h2>
                                <div class="row">
                                    <div class="col-md-6 col-12">
                                        <div class="form-group">
                                            <input type="text" class="form-control" name="fname" placeholder="First Name*" required>
                                        </div>
                                    </div>
                                    <div class="col-md-6 col-12">
                                        <div class="form-group">
                                            <input type="text" class="form-control" name="lname" placeholder="Last Name*" required>
                                        </div>
                                    </div>
                                    <div class="col-md-6 col-12">
                                        <div class="form-group">
                                            <input type="email" class="form-control" name="email" placeholder="Email Address*" required>
                                        </div>
                                    </div>
                                    <div class="col-md-6 col-12">
                                        <div class="form-group">
                                            <select name="cause" class="form-control">
                                                <option selected>General Mosque Fund</option>
                                                <option>Quran Teacher &amp; Student Sponsorship</option>
                                                <option>Zakat-ul-Mal (Obligatory Charity)</option>
                                                <option>Ramadan Iftar &amp; Food Relief</option>
                                                <option>Community Orphan Support</option>
                                            </select>
                                        </div>
                                    </div>
                                    <div class="col-12">
                                        <textarea class="form-control" name="notes" placeholder="Special Note or In Memory Of (Optional)"></textarea>
                                    </div>
                                </div>
                            </div>
                            <div class="wpo-doanation-payment">
                                <h2>3. Payment Method</h2>
                                <div class="payment-options" style="margin-bottom: 25px;">
                                    <label style="margin-right: 25px; cursor: pointer; font-size: 16px;">
                                        <input type="radio" name="payment_method" value="card" checked> Credit / Debit Card
                                    </label>
                                    <label style="margin-right: 25px; cursor: pointer; font-size: 16px;">
                                        <input type="radio" name="payment_method" value="paypal"> PayPal
                                    </label>
                                    <label style="cursor: pointer; font-size: 16px;">
                                        <input type="radio" name="payment_method" value="bank"> Bank Transfer / Cash
                                    </label>
                                </div>
                                <div class="submit-area text-center">
                                    <button type="submit" class="theme-btn" style="padding: 15px 45px; font-size: 18px;">Complete Donation</button>
                                </div>
                                <div id="donate-success" style="display:none; margin-top: 20px; padding: 15px; background: #e8f5e9; border: 1px solid #c8e6c9; border-radius: 4px; color: #2e7d32; text-align: center; font-weight: 600;">
                                    May Allah accept your generous donation and reward you abundantly in this life and the Hereafter.
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </section>
`;

// 4. SHOP PAGE
const shopContent = `
        <!-- start of wpo-shop-section -->
        <section class="wpo-shop-section section-padding">
            <div class="container">
                <div class="row">
                    <div class="col col-xs-12">
                        <div class="shop-grids clearfix">
                            <div class="grid">
                                <div class="img-holder">
                                    <img src="assets/images/page-title.jpg" alt="Holy Quran Tajweed" style="height: 250px; object-fit: cover;">
                                </div>
                                <div class="details">
                                    <h3><a href="shop-single.html">Holy Quran (Tajweed Edition)</a></h3>
                                    <del>$35.00</del>
                                    <span>$25.00</span>
                                    <div class="add-to-cart">
                                        <a href="cart.html">Add to cart <i class="ti-shopping-cart"></i></a>
                                    </div>
                                </div>
                            </div>
                            <div class="grid">
                                <div class="img-holder">
                                    <img src="assets/images/page-title.jpg" alt="Prayer Rug" style="height: 250px; object-fit: cover;">
                                </div>
                                <div class="details">
                                    <h3><a href="shop-single.html">Premium Velvet Prayer Rug</a></h3>
                                    <del>$45.00</del>
                                    <span>$35.00</span>
                                    <div class="add-to-cart">
                                        <a href="cart.html">Add to cart <i class="ti-shopping-cart"></i></a>
                                    </div>
                                </div>
                            </div>
                            <div class="grid">
                                <div class="img-holder">
                                    <img src="assets/images/page-title.jpg" alt="Royal Amber Attar" style="height: 250px; object-fit: cover;">
                                </div>
                                <div class="details">
                                    <h3><a href="shop-single.html">Royal Amber &amp; Oud Attar (12ml)</a></h3>
                                    <del>$28.00</del>
                                    <span>$20.15</span>
                                    <div class="add-to-cart">
                                        <a href="cart.html">Add to cart <i class="ti-shopping-cart"></i></a>
                                    </div>
                                </div>
                            </div>
                            <div class="grid">
                                <div class="img-holder">
                                    <img src="assets/images/page-title.jpg" alt="Wooden Rehal Stand" style="height: 250px; object-fit: cover;">
                                </div>
                                <div class="details">
                                    <h3><a href="shop-single.html">Handcrafted Wooden Quran Stand</a></h3>
                                    <del>$50.00</del>
                                    <span>$39.99</span>
                                    <div class="add-to-cart">
                                        <a href="cart.html">Add to cart <i class="ti-shopping-cart"></i></a>
                                    </div>
                                </div>
                            </div>
                            <div class="grid">
                                <div class="img-holder">
                                    <img src="assets/images/page-title.jpg" alt="Muslim Prayer Hat" style="height: 250px; object-fit: cover;">
                                </div>
                                <div class="details">
                                    <h3><a href="shop-single.html">Embroidered Muslim Kufi Hat</a></h3>
                                    <del>$18.00</del>
                                    <span>$13.25</span>
                                    <div class="add-to-cart">
                                        <a href="cart.html">Add to cart <i class="ti-shopping-cart"></i></a>
                                    </div>
                                </div>
                            </div>
                            <div class="grid">
                                <div class="img-holder">
                                    <img src="assets/images/page-title.jpg" alt="Digital Tasbih" style="height: 250px; object-fit: cover;">
                                </div>
                                <div class="details">
                                    <h3><a href="shop-single.html">Digital Tasbih Counter &amp; Ring</a></h3>
                                    <del>$16.00</del>
                                    <span>$11.50</span>
                                    <div class="add-to-cart">
                                        <a href="cart.html">Add to cart <i class="ti-shopping-cart"></i></a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
`;

// 5. CART PAGE
const cartContent = `
        <!-- start of cart-section -->
        <section class="cart-section section-padding">
            <div class="container">
                <div class="row">
                    <div class="col col-xs-12">
                        <div class="cart-area">
                            <form action="#" method="post">
                                <div class="table-responsive">
                                    <table class="table table-bordered text-center">
                                        <thead style="background: #f8f8f8;">
                                            <tr>
                                                <th>Product</th>
                                                <th>Name</th>
                                                <th>Price</th>
                                                <th>Quantity</th>
                                                <th>Total</th>
                                                <th>Remove</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr>
                                                <td style="width: 100px;">
                                                    <img src="assets/images/page-title.jpg" alt="Attar" style="width: 60px; height: 60px; object-fit: cover; border-radius: 4px;">
                                                </td>
                                                <td style="vertical-align: middle; font-weight: 600;">Royal Amber &amp; Oud Perfume</td>
                                                <td style="vertical-align: middle;">$20.15</td>
                                                <td style="vertical-align: middle; width: 120px;">
                                                    <input type="number" class="form-control text-center" value="1" min="1" max="99">
                                                </td>
                                                <td style="vertical-align: middle; font-weight: 700; color: #DB9E30;">$20.15</td>
                                                <td style="vertical-align: middle;">
                                                    <button type="button" class="btn btn-sm btn-outline-danger" onclick="this.closest('tr').remove();"><i class="ti-trash"></i></button>
                                                </td>
                                            </tr>
                                            <tr>
                                                <td style="width: 100px;">
                                                    <img src="assets/images/page-title.jpg" alt="Hat" style="width: 60px; height: 60px; object-fit: cover; border-radius: 4px;">
                                                </td>
                                                <td style="vertical-align: middle; font-weight: 600;">Muslim Kufi Hat</td>
                                                <td style="vertical-align: middle;">$13.25</td>
                                                <td style="vertical-align: middle; width: 120px;">
                                                    <input type="number" class="form-control text-center" value="2" min="1" max="99">
                                                </td>
                                                <td style="vertical-align: middle; font-weight: 700; color: #DB9E30;">$26.50</td>
                                                <td style="vertical-align: middle;">
                                                    <button type="button" class="btn btn-sm btn-outline-danger" onclick="this.closest('tr').remove();"><i class="ti-trash"></i></button>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </div>
                                <div class="cart-action-btn" style="display: flex; justify-content: space-between; margin-top: 25px; flex-wrap: wrap; gap: 15px;">
                                    <a href="shop.html" class="theme-btn s2">Continue Shopping</a>
                                    <a href="checkout.html" class="theme-btn">Proceed to Checkout</a>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </section>
`;

// 6. CHECKOUT PAGE
const checkoutContent = `
        <!-- start of checkout-section -->
        <section class="checkout-section section-padding">
            <div class="container">
                <div class="row">
                    <div class="col-lg-7 col-12">
                        <div class="wpo-checkout-area">
                            <h3 style="margin-bottom: 25px; font-weight: 700;">Billing Details</h3>
                            <form action="#" method="post" id="checkout-form" onsubmit="event.preventDefault(); document.getElementById('order-confirmed').style.display='block';">
                                <div class="row">
                                    <div class="col-md-6 col-12 mb-3">
                                        <label>First Name*</label>
                                        <input type="text" class="form-control" required>
                                    </div>
                                    <div class="col-md-6 col-12 mb-3">
                                        <label>Last Name*</label>
                                        <input type="text" class="form-control" required>
                                    </div>
                                    <div class="col-12 mb-3">
                                        <label>Street Address*</label>
                                        <input type="text" class="form-control" placeholder="House number and street name" required>
                                    </div>
                                    <div class="col-md-6 col-12 mb-3">
                                        <label>Town / City*</label>
                                        <input type="text" class="form-control" required>
                                    </div>
                                    <div class="col-md-6 col-12 mb-3">
                                        <label>Postcode / ZIP*</label>
                                        <input type="text" class="form-control" required>
                                    </div>
                                    <div class="col-md-6 col-12 mb-3">
                                        <label>Phone*</label>
                                        <input type="text" class="form-control" required>
                                    </div>
                                    <div class="col-md-6 col-12 mb-3">
                                        <label>Email Address*</label>
                                        <input type="email" class="form-control" required>
                                    </div>
                                </div>
                                <div class="submit-btn-area" style="margin-top: 30px;">
                                    <button type="submit" class="theme-btn" style="width: 100%; padding: 15px;">Place Order</button>
                                </div>
                                <div id="order-confirmed" style="display:none; margin-top: 20px; padding: 20px; background: #e8f5e9; border: 1px solid #a5d6a7; border-radius: 4px; color: #1b5e20; text-align: center; font-weight: 600;">
                                    JazakAllah Khair! Your order #IST-9842 has been successfully placed. A confirmation email has been dispatched.
                                </div>
                            </form>
                        </div>
                    </div>
                    <div class="col-lg-5 col-12">
                        <div style="background: #fbfbfb; padding: 35px; border: 1px solid #ebebeb; border-radius: 6px;">
                            <h3 style="font-weight: 700; margin-bottom: 20px;">Your Order</h3>
                            <ul style="list-style: none; padding: 0; margin-bottom: 25px;">
                                <li style="display: flex; justify-content: space-between; padding: 10px 0; border-bottom: 1px solid #eee;">
                                    <span>Royal Amber &amp; Oud (x1)</span>
                                    <strong>$20.15</strong>
                                </li>
                                <li style="display: flex; justify-content: space-between; padding: 10px 0; border-bottom: 1px solid #eee;">
                                    <span>Muslim Kufi Hat (x2)</span>
                                    <strong>$26.50</strong>
                                </li>
                                <li style="display: flex; justify-content: space-between; padding: 10px 0; border-bottom: 1px solid #eee;">
                                    <span>Shipping</span>
                                    <strong>Free</strong>
                                </li>
                                <li style="display: flex; justify-content: space-between; padding: 15px 0; font-size: 20px; font-weight: 700;">
                                    <span>Total:</span>
                                    <span style="color: #DB9E30;">$46.65</span>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </section>
`;

// 7. LOGIN PAGE
const loginContent = `
        <!-- start of login section -->
        <section class="wpo-login-area">
            <div class="container">
                <div class="row">
                    <div class="col-lg-6 offset-lg-3 col-md-8 offset-md-2 col-12">
                        <div style="background: #fff; padding: 45px 35px; box-shadow: 0 5px 25px rgba(0,0,0,0.08); border-radius: 8px; border: 1px solid #ebebeb;">
                            <div class="text-center" style="margin-bottom: 30px;">
                                <h2 style="font-weight: 700;">Sign In</h2>
                                <p style="color: #666; margin-top: 8px;">Access the Quran Teacher &amp; Student Portal</p>
                            </div>
                            <form action="#" method="post" onsubmit="event.preventDefault(); alert('Signed in successfully.');">
                                <div class="form-group mb-3">
                                    <label style="font-weight: 600; margin-bottom: 6px;">Email Address</label>
                                    <input type="email" class="form-control" placeholder="yourname@gmail.com" required>
                                </div>
                                <div class="form-group mb-3">
                                    <label style="font-weight: 600; margin-bottom: 6px;">Password</label>
                                    <input type="password" class="form-control" placeholder="••••••••" required>
                                </div>
                                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 25px;">
                                    <label style="margin: 0; cursor: pointer;">
                                        <input type="checkbox"> Remember me
                                    </label>
                                    <a href="forgot.html" style="color: #DB9E30;">Forgot password?</a>
                                </div>
                                <button type="submit" class="theme-btn" style="width: 100%; padding: 12px;">Sign In</button>
                                <div class="text-center" style="margin-top: 25px;">
                                    <p style="margin-bottom: 0;">Don't have an account? <a href="register.html" style="color: #DB9E30; font-weight: 600;">Create Account</a></p>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </section>
`;

// 8. REGISTER PAGE
const registerContent = `
        <!-- start of register section -->
        <section class="wpo-login-area">
            <div class="container">
                <div class="row">
                    <div class="col-lg-6 offset-lg-3 col-md-8 offset-md-2 col-12">
                        <div style="background: #fff; padding: 45px 35px; box-shadow: 0 5px 25px rgba(0,0,0,0.08); border-radius: 8px; border: 1px solid #ebebeb;">
                            <div class="text-center" style="margin-bottom: 30px;">
                                <h2 style="font-weight: 700;">Create an Account</h2>
                                <p style="color: #666; margin-top: 8px;">Register for Online Quran Classes &amp; Programs</p>
                            </div>
                            <form action="#" method="post" onsubmit="event.preventDefault(); alert('Account registered successfully! Welcome to Quran Teacher.');">
                                <div class="form-group mb-3">
                                    <label style="font-weight: 600; margin-bottom: 6px;">Full Name</label>
                                    <input type="text" class="form-control" placeholder="Muhammad Ali" required>
                                </div>
                                <div class="form-group mb-3">
                                    <label style="font-weight: 600; margin-bottom: 6px;">Email Address</label>
                                    <input type="email" class="form-control" placeholder="yourname@gmail.com" required>
                                </div>
                                <div class="form-group mb-3">
                                    <label style="font-weight: 600; margin-bottom: 6px;">Password</label>
                                    <input type="password" class="form-control" placeholder="Create strong password" required>
                                </div>
                                <div class="form-group mb-3">
                                    <label style="font-weight: 600; margin-bottom: 6px;">Confirm Password</label>
                                    <input type="password" class="form-control" placeholder="Confirm your password" required>
                                </div>
                                <div style="margin-bottom: 25px;">
                                    <label style="margin: 0; cursor: pointer;">
                                        <input type="checkbox" required> I agree to the <a href="terms.html" style="color: #DB9E30;">Terms of Service</a> and <a href="privace.html" style="color: #DB9E30;">Privacy Policy</a>
                                    </label>
                                </div>
                                <button type="submit" class="theme-btn" style="width: 100%; padding: 12px;">Register Now</button>
                                <div class="text-center" style="margin-top: 25px;">
                                    <p style="margin-bottom: 0;">Already have an account? <a href="login.html" style="color: #DB9E30; font-weight: 600;">Sign In</a></p>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </section>
`;

// 9. FORGOT PASSWORD
const forgotContent = `
        <section class="wpo-login-area">
            <div class="container">
                <div class="row">
                    <div class="col-lg-6 offset-lg-3 col-md-8 offset-md-2 col-12">
                        <div style="background: #fff; padding: 45px 35px; box-shadow: 0 5px 25px rgba(0,0,0,0.08); border-radius: 8px; border: 1px solid #ebebeb;">
                            <div class="text-center" style="margin-bottom: 30px;">
                                <h2 style="font-weight: 700;">Reset Password</h2>
                                <p style="color: #666; margin-top: 8px;">Enter your registered email to receive a password reset link.</p>
                            </div>
                            <form action="#" method="post" onsubmit="event.preventDefault(); document.getElementById('reset-sent').style.display='block';">
                                <div class="form-group mb-3">
                                    <label style="font-weight: 600; margin-bottom: 6px;">Email Address</label>
                                    <input type="email" class="form-control" placeholder="yourname@gmail.com" required>
                                </div>
                                <button type="submit" class="theme-btn" style="width: 100%; padding: 12px;">Send Recovery Link</button>
                                <div id="reset-sent" style="display:none; margin-top: 15px; color: green; text-align: center; font-weight: 600;">
                                    A password reset link has been dispatched to your email.
                                </div>
                                <div class="text-center" style="margin-top: 25px;">
                                    <p style="margin-bottom: 0;">Remembered your password? <a href="login.html" style="color: #DB9E30; font-weight: 600;">Sign In</a></p>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </section>
`;

// 10. 404 PAGE
const errorContent = `
        <section class="error-404-section section-padding">
            <div class="container">
                <div class="row">
                    <div class="col col-xs-12 text-center">
                        <div class="content clearfix">
                            <div class="error-message" style="margin: 60px auto; max-width: 600px;">
                                <h1 style="font-size: 110px; font-weight: 900; color: #DB9E30; margin-bottom: 15px;">404</h1>
                                <h3 style="font-size: 28px; font-weight: 700; margin-bottom: 15px;">Page Not Found</h3>
                                <p style="color: #666; margin-bottom: 30px; font-size: 16px;">We're sorry, but the page you are looking for does not exist or has been relocated.</p>
                                <a href="index.html" class="theme-btn">Back to Home</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
`;

// 11. BLOG PAGE
const blogContent = `
        <section class="wpo-blog-pg-section section-padding">
            <div class="container">
                <div class="row">
                    <div class="col-lg-8 col-12">
                        <div class="wpo-blog-content">
                            <div class="post format-standard-image mb-5" style="border: 1px solid #ebebeb; border-radius: 6px; overflow: hidden; background: #fff;">
                                <div class="entry-media">
                                    <img src="assets/images/page-title.jpg" alt="Quran Article" style="width: 100%; height: 320px; object-fit: cover;">
                                </div>
                                <div class="entry-meta" style="padding: 20px 25px 0; color: #888; font-size: 14px;">
                                    <span><i class="ti-calendar"></i> September 12, 2026</span> &nbsp;|&nbsp;
                                    <span><i class="ti-user"></i> Sheikh Dr. Ahmad</span> &nbsp;|&nbsp;
                                    <span><i class="ti-comment"></i> 5 Comments</span>
                                </div>
                                <div class="entry-details" style="padding: 15px 25px 30px;">
                                    <h3 style="font-weight: 700; margin-bottom: 15px;"><a href="blog-single.html" style="color: #222;">The Immense Spiritual Rewards of Daily Quran Recitation with Tajweed</a></h3>
                                    <p style="color: #666; line-height: 1.7;">Reciting the Quran brings tranquility to the heart and elevates one's status in this world and the Hereafter. Tajweed ensures that every letter is pronounced with its rightful attributes and articulators...</p>
                                    <a href="blog-single.html" class="theme-btn s2" style="margin-top: 10px;">Read More</a>
                                </div>
                            </div>
                            <div class="post format-standard-image mb-5" style="border: 1px solid #ebebeb; border-radius: 6px; overflow: hidden; background: #fff;">
                                <div class="entry-media">
                                    <img src="assets/images/page-title.jpg" alt="Family Education" style="width: 100%; height: 320px; object-fit: cover;">
                                </div>
                                <div class="entry-meta" style="padding: 20px 25px 0; color: #888; font-size: 14px;">
                                    <span><i class="ti-calendar"></i> September 05, 2026</span> &nbsp;|&nbsp;
                                    <span><i class="ti-user"></i> Ustadh Tariq</span> &nbsp;|&nbsp;
                                    <span><i class="ti-comment"></i> 8 Comments</span>
                                </div>
                                <div class="entry-details" style="padding: 15px 25px 30px;">
                                    <h3 style="font-weight: 700; margin-bottom: 15px;"><a href="blog-single.html" style="color: #222;">Nurturing Islamic Values &amp; Character in the Younger Generation</a></h3>
                                    <p style="color: #666; line-height: 1.7;">Raising children with solid moral foundations is one of the greatest responsibilities bestowed upon parents. Learn how our youth academy integrates ethics, prophetic stories, and interactive learning...</p>
                                    <a href="blog-single.html" class="theme-btn s2" style="margin-top: 10px;">Read More</a>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-4 col-12">
                        <div class="blog-sidebar" style="background: #fafafa; padding: 30px; border: 1px solid #ebebeb; border-radius: 6px;">
                            <div class="widget search-widget mb-4">
                                <h3 style="font-size: 20px; font-weight: 700; margin-bottom: 15px;">Search Blog</h3>
                                <form action="#" method="get">
                                    <div class="input-group">
                                        <input type="text" class="form-control" placeholder="Search topics...">
                                        <button class="btn theme-btn" type="submit"><i class="ti-search"></i></button>
                                    </div>
                                </form>
                            </div>
                            <div class="widget category-widget mb-4">
                                <h3 style="font-size: 20px; font-weight: 700; margin-bottom: 15px;">Categories</h3>
                                <ul style="list-style: none; padding: 0;">
                                    <li style="padding: 8px 0; border-bottom: 1px solid #eee;"><a href="blog.html" style="color: #555;">Quran &amp; Tajweed (14)</a></li>
                                    <li style="padding: 8px 0; border-bottom: 1px solid #eee;"><a href="blog.html" style="color: #555;">Hadith &amp; Sunnah (9)</a></li>
                                    <li style="padding: 8px 0; border-bottom: 1px solid #eee;"><a href="blog.html" style="color: #555;">Islamic Parenting (12)</a></li>
                                    <li style="padding: 8px 0; border-bottom: 1px solid #eee;"><a href="blog.html" style="color: #555;">Charity &amp; Community (7)</a></li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
`;

// 12. BLOG SINGLE
const blogSingleContent = `
        <section class="wpo-blog-single-section section-padding">
            <div class="container">
                <div class="row">
                    <div class="col-lg-8 col-12">
                        <div class="wpo-blog-content" style="background: #fff; padding: 35px; border: 1px solid #ebebeb; border-radius: 6px;">
                            <div class="entry-media mb-4">
                                <img src="assets/images/page-title.jpg" alt="Quran Blog" style="width: 100%; height: 380px; object-fit: cover; border-radius: 6px;">
                            </div>
                            <div class="entry-meta mb-3" style="color: #888; font-size: 14px;">
                                <span><i class="ti-calendar"></i> September 12, 2026</span> &nbsp;|&nbsp;
                                <span><i class="ti-user"></i> Sheikh Dr. Ahmad</span> &nbsp;|&nbsp;
                                <span><i class="ti-tag"></i> Quran &amp; Tajweed</span>
                            </div>
                            <h2 style="font-weight: 700; margin-bottom: 20px;">The Immense Spiritual Rewards of Daily Quran Recitation with Tajweed</h2>
                            <p style="color: #555; line-height: 1.8; font-size: 16px;">The Noble Quran is the direct word of Allah Subhanahu Wa Ta'ala, sent down as guidance, mercy, and light for all mankind. Engaging with the Quran every day elevates the soul, removes sorrow from the heart, and invites blessings into the home.</p>
                            <blockquote style="border-left: 4px solid #DB9E30; padding: 20px 25px; margin: 30px 0; background: #fdfbf7; font-style: italic; font-size: 18px; color: #333;">
                                "The best among you are those who learn the Quran and teach it to others." — Sahih Al-Bukhari
                            </blockquote>
                            <p style="color: #555; line-height: 1.8; font-size: 16px;">When reciting with Tajweed, we honor the speech of our Creator by enunciating letters precisely from their proper vocal points (Makharij) and applying their inherent characteristics (Sifaat). At Istiqbal Islamic Centre, our certified instructors guide students step-by-step to achieve fluent and melodic recitation.</p>
                            <div style="margin-top: 35px; padding-top: 25px; border-top: 1px solid #eee;">
                                <a href="blog.html" class="theme-btn s2"><i class="ti-arrow-left"></i> Back to All Articles</a>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-4 col-12">
                        <div class="blog-sidebar" style="background: #fafafa; padding: 30px; border: 1px solid #ebebeb; border-radius: 6px;">
                            <h3 style="font-size: 20px; font-weight: 700; margin-bottom: 15px;">About the Author</h3>
                            <p style="color: #666; font-size: 15px; line-height: 1.6;">Sheikh Dr. Ahmad Al-Mansoor holds an Ijazah in the Ten Qira'at and serves as Senior Instructor at Istiqbal Islamic Centre.</p>
                            <h3 style="font-size: 20px; font-weight: 700; margin-top: 30px; margin-bottom: 15px;">Need Quran Guidance?</h3>
                            <a href="service.html" class="theme-btn" style="width: 100%; text-align: center;">Enroll in Classes</a>
                        </div>
                    </div>
                </div>
            </div>
        </section>
`;

// 13. EVENT SINGLE
const eventSingleContent = `
        <section class="wpo-event-details-area section-padding">
            <div class="container">
                <div class="row">
                    <div class="col-lg-8 col-12">
                        <div class="wpo-event-details-wrap" style="background: #fff; padding: 35px; border: 1px solid #ebebeb; border-radius: 6px;">
                            <div class="wpo-event-details-img mb-4">
                                <img src="assets/images/page-title.jpg" alt="Event Banner" style="width: 100%; height: 380px; object-fit: cover; border-radius: 6px;">
                            </div>
                            <div class="wpo-event-details-text">
                                <h2 style="font-weight: 700; margin-bottom: 15px;">Annual Islamic Conference &amp; Community Gathering 2026</h2>
                                <p style="color: #666; line-height: 1.8; font-size: 16px;">Join scholars, families, and youth for our premier annual conference celebrating unity, Islamic scholarship, and spiritual rejuvenation. Featuring keynote lectures, breakout workshops, and youth competitions.</p>
                                <div class="wpo-event-details-tab" style="margin-top: 30px;">
                                    <ul class="nav nav-tabs" style="border-bottom: 2px solid #DB9E30;">
                                        <li class="nav-item"><a class="nav-link active" href="#schedule">Event Schedule</a></li>
                                        <li class="nav-item"><a class="nav-link" href="#speakers">Guest Speakers</a></li>
                                        <li class="nav-item"><a class="nav-link" href="#venue">Location &amp; Parking</a></li>
                                    </ul>
                                    <div class="tab-content" style="padding: 25px 0;">
                                        <div id="schedule" class="tab-pane active">
                                            <ul style="list-style: none; padding: 0; line-height: 2;">
                                                <li><strong>09:00 AM:</strong> Welcome Reception &amp; Quran Opening Recitation</li>
                                                <li><strong>10:30 AM:</strong> Keynote Lecture: Faith in the Modern Era</li>
                                                <li><strong>01:30 PM:</strong> Dhuhr Prayer &amp; Community Lunch</li>
                                                <li><strong>03:00 PM:</strong> Youth Workshop &amp; Q&amp;A Session</li>
                                                <li><strong>05:30 PM:</strong> Closing Dua &amp; Awards Ceremony</li>
                                            </ul>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-4 col-12">
                        <div style="background: #fcfcfc; padding: 30px; border: 1px solid #ebebeb; border-radius: 6px;">
                            <h3 style="font-size: 22px; font-weight: 700; margin-bottom: 20px;">Event Details</h3>
                            <ul style="list-style: none; padding: 0; line-height: 2.2; color: #555;">
                                <li><i class="ti-calendar" style="color: #DB9E30; margin-right: 8px;"></i> <strong>Date:</strong> October 25, 2026</li>
                                <li><i class="ti-time" style="color: #DB9E30; margin-right: 8px;"></i> <strong>Time:</strong> 09:00 AM - 06:00 PM</li>
                                <li><i class="ti-location-pin" style="color: #DB9E30; margin-right: 8px;"></i> <strong>Venue:</strong> Istiqbal Main Auditorium</li>
                                <li><i class="ti-ticket" style="color: #DB9E30; margin-right: 8px;"></i> <strong>Admission:</strong> Free (RSVP Required)</li>
                            </ul>
                            <a href="contact.html" class="theme-btn" style="width: 100%; text-align: center; margin-top: 20px;">Register Your Seat</a>
                        </div>
                    </div>
                </div>
            </div>
        </section>
`;

// 14. SERVICE SINGLE
const serviceSingleContent = `
        <section class="wpo-service-details-area section-padding">
            <div class="container">
                <div class="row">
                    <div class="col-lg-8 col-12">
                        <div class="wpo-service-details-wrap" style="background: #fff; padding: 35px; border: 1px solid #ebebeb; border-radius: 6px;">
                            <div class="wpo-service-details-img mb-4">
                                <img src="assets/images/page-title.jpg" alt="Service Details" style="width: 100%; height: 380px; object-fit: cover; border-radius: 6px;">
                            </div>
                            <h2 style="font-weight: 700; margin-bottom: 15px;">One-on-One Quran Recitation &amp; Tajweed Mastery</h2>
                            <p style="color: #666; line-height: 1.8; font-size: 16px;">Our online and in-person Quran classes provide customized curriculum for both beginners and advanced students. Taught by certified scholars from reputable Islamic universities, learners progress smoothly through phonetics, word construction, and fluent Surah recitation.</p>
                            <h3 style="font-size: 22px; font-weight: 700; margin: 25px 0 15px;">Program Highlights</h3>
                            <ul style="color: #555; line-height: 2; padding-left: 20px;">
                                <li>Flexible class schedules suited for students and working professionals</li>
                                <li>Individualized 1-on-1 attention with male and female instructors</li>
                                <li>Noorani Qaida foundation for beginners</li>
                                <li>Detailed articulation and rules of Tajweed (Makharij, Ghunnah, Ikhfa, Idgham)</li>
                                <li>Hifz (memorization) tracks with regular revision tracking</li>
                            </ul>
                            <div style="margin-top: 30px;">
                                <a href="contact.html" class="theme-btn">Book a Free Trial Session</a>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-4 col-12">
                        <div style="background: #fbfbfb; padding: 30px; border: 1px solid #ebebeb; border-radius: 6px;">
                            <h3 style="font-size: 20px; font-weight: 700; margin-bottom: 20px;">All Services</h3>
                            <ul style="list-style: none; padding: 0; line-height: 2.2;">
                                <li style="border-bottom: 1px solid #eee;"><a href="service-single.html" style="color: #DB9E30; font-weight: 600;">Quran Teaching &amp; Tajweed</a></li>
                                <li style="border-bottom: 1px solid #eee;"><a href="service-single.html" style="color: #555;">Hifz Program</a></li>
                                <li style="border-bottom: 1px solid #eee;"><a href="service-single.html" style="color: #555;">Islamic Jurisprudence (Fiqh)</a></li>
                                <li style="border-bottom: 1px solid #eee;"><a href="service-single.html" style="color: #555;">Marriage &amp; Nikah Services</a></li>
                                <li style="border-bottom: 1px solid #eee;"><a href="service-single.html" style="color: #555;">Funeral &amp; Janazah Services</a></li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </section>
`;

// 15. TERMS & CONDITIONS
const termsContent = `
        <section class="pf-terms-section section-padding">
            <div class="container">
                <div class="row">
                    <div class="col-lg-10 offset-lg-1 col-12">
                        <div style="background: #fff; padding: 40px; border: 1px solid #ebebeb; border-radius: 6px;">
                            <h2 style="font-weight: 700; margin-bottom: 20px;">Terms and Conditions</h2>
                            <p style="color: #666; line-height: 1.8;">Welcome to Istiqbal Islamic Centre &amp; Quran Teacher. By accessing our website, enrolling in courses, or attending programs, you agree to comply with our terms and respectful conduct guidelines.</p>
                            <h4 style="margin-top: 25px; font-weight: 700;">1. Course Enrollment and Attendance</h4>
                            <p style="color: #666; line-height: 1.8;">Students are expected to arrive punctually for online sessions and maintain a respectful learning environment adhering to Islamic etiquette.</p>
                            <h4 style="margin-top: 25px; font-weight: 700;">2. Donations and Payments</h4>
                            <p style="color: #666; line-height: 1.8;">All donations given to Istiqbal Islamic Centre are dedicated transparently toward their designated causes (General Mosque Fund, Zakat, Quran Sponsorship).</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
`;

// 16. PRIVACY POLICY
const privaceContent = `
        <section class="pf-terms-section section-padding">
            <div class="container">
                <div class="row">
                    <div class="col-lg-10 offset-lg-1 col-12">
                        <div style="background: #fff; padding: 40px; border: 1px solid #ebebeb; border-radius: 6px;">
                            <h2 style="font-weight: 700; margin-bottom: 20px;">Privacy Policy</h2>
                            <p style="color: #666; line-height: 1.8;">At Istiqbal Islamic Centre, your privacy is of paramount importance to us. This privacy policy explains how we handle your personal data when using our website and services.</p>
                            <h4 style="margin-top: 25px; font-weight: 700;">Information We Collect</h4>
                            <p style="color: #666; line-height: 1.8;">We collect contact information such as name, email address, and phone number when you register for classes, submit inquiries, or make donations.</p>
                            <h4 style="margin-top: 25px; font-weight: 700;">Data Security</h4>
                            <p style="color: #666; line-height: 1.8;">Your personal information is strictly protected and never sold or shared with external third parties without your explicit consent.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
`;

const pages = [
  { file: 'about.html', title: 'About Us', desc: 'Learn about Istiqbal Islamic Centre and our Quran teaching mission', breadcrumb: 'About Us', content: aboutContent },
  { file: 'contact.html', title: 'Contact Us', desc: 'Get in touch with Istiqbal Islamic Centre and Quran teachers', breadcrumb: 'Contact Us', content: contactContent },
  { file: 'donate.html', title: 'Donate Now', desc: 'Support Islamic education, mosque expansion, and charity funds', breadcrumb: 'Donate Now', content: donateContent },
  { file: 'shop.html', title: 'Islamic Shop', desc: 'Shop Quran copies, prayer rugs, attar perfumes, and accessories', breadcrumb: 'Shop', content: shopContent },
  { file: 'shop-single.html', title: 'Product Details', desc: 'Explore Islamic books, prayer essentials, and gifts', breadcrumb: 'Product Details', content: shopContent },
  { file: 'cart.html', title: 'Shopping Cart', desc: 'Review items in your shopping cart', breadcrumb: 'Cart', content: cartContent },
  { file: 'checkout.html', title: 'Checkout', desc: 'Secure checkout for Islamic store orders', breadcrumb: 'Checkout', content: checkoutContent },
  { file: 'login.html', title: 'Sign In', desc: 'Sign in to the Quran Teacher and student portal', breadcrumb: 'Sign In', content: loginContent },
  { file: 'register.html', title: 'Register', desc: 'Create an account for online Quran classes', breadcrumb: 'Register', content: registerContent },
  { file: 'forgot.html', title: 'Reset Password', desc: 'Recover your account password', breadcrumb: 'Forgot Password', content: forgotContent },
  { file: '404.html', title: 'Page Not Found', desc: 'The requested page was not found', breadcrumb: '404 Error', content: errorContent },
  { file: 'blog.html', title: 'Islamic Blog', desc: 'Read Islamic articles, Quran reflections, and community news', breadcrumb: 'Blog', content: blogContent },
  { file: 'blog-left-sidebar.html', title: 'Islamic Blog', desc: 'Read Islamic articles, Quran reflections, and community news', breadcrumb: 'Blog', content: blogContent },
  { file: 'blog-fullwidth.html', title: 'Islamic Blog', desc: 'Read Islamic articles, Quran reflections, and community news', breadcrumb: 'Blog', content: blogContent },
  { file: 'blog-single.html', title: 'Article Details', desc: 'In-depth Islamic article and discussion', breadcrumb: 'Blog Details', content: blogSingleContent },
  { file: 'blog-single-left-sidebar.html', title: 'Article Details', desc: 'In-depth Islamic article and discussion', breadcrumb: 'Blog Details', content: blogSingleContent },
  { file: 'blog-single-fullwidth.html', title: 'Article Details', desc: 'In-depth Islamic article and discussion', breadcrumb: 'Blog Details', content: blogSingleContent },
  { file: 'event-single.html', title: 'Event Details', desc: 'Conference and gathering details at Istiqbal Centre', breadcrumb: 'Event Details', content: eventSingleContent },
  { file: 'event-s2.html', title: 'Events', desc: 'Upcoming Islamic events and community gatherings', breadcrumb: 'Event Style 2', content: eventContentFromExisting() },
  { file: 'service-single.html', title: 'Service Details', desc: 'Explore our Quran recitation and Islamic educational courses', breadcrumb: 'Service Details', content: serviceSingleContent },
  { file: 'service-s2.html', title: 'Services', desc: 'Explore Islamic educational courses and community programs', breadcrumb: 'Service Style 2', content: serviceContentFromExisting() },
  { file: 'terms.html', title: 'Terms & Conditions', desc: 'Terms of service and policies of Istiqbal Islamic Centre', breadcrumb: 'Terms & Conditions', content: termsContent },
  { file: 'privace.html', title: 'Privacy Policy', desc: 'Privacy policy and data protection at Istiqbal Islamic Centre', breadcrumb: 'Privacy Policy', content: privaceContent },
  { file: 'privacy.html', title: 'Privacy Policy', desc: 'Privacy policy and data protection at Istiqbal Islamic Centre', breadcrumb: 'Privacy Policy', content: privaceContent },
];

function eventContentFromExisting() {
  const fileContent = fs.readFileSync('public/event.html', 'utf8');
  const breadcrumbEnd = fileContent.indexOf('<!-- end of breadcumb -->');
  const footerStart = fileContent.indexOf('<!-- start of footer-section -->');
  if (breadcrumbEnd !== -1 && footerStart !== -1) {
    return fileContent.substring(breadcrumbEnd + '<!-- end of breadcumb -->'.length, footerStart);
  }
  return '';
}

function serviceContentFromExisting() {
  const fileContent = fs.readFileSync('public/service.html', 'utf8');
  const breadcrumbEnd = fileContent.indexOf('<!-- end of breadcumb -->');
  const footerStart = fileContent.indexOf('<!-- start of footer-section -->');
  if (breadcrumbEnd !== -1 && footerStart !== -1) {
    return fileContent.substring(breadcrumbEnd + '<!-- end of breadcumb -->'.length, footerStart);
  }
  return '';
}

for (const p of pages) {
  const html = createPage(p.title, p.desc, p.breadcrumb, p.content);
  fs.writeFileSync(path.join('public', p.file), html, 'utf8');
  console.log(`Generated public/${p.file}`);
}

// Also create index-2.html and index-3.html from index.html
const indexHtml = fs.readFileSync('public/index.html', 'utf8');
fs.writeFileSync('public/index-2.html', indexHtml, 'utf8');
fs.writeFileSync('public/index-3.html', indexHtml, 'utf8');
console.log('Generated index-2.html and index-3.html');
