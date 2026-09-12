(function($) {
  "use strict";

  // Preloader
  function handlePreloader() {
    var preloader = document.querySelector('.preloader');
    if (preloader) {
      preloader.style.transition = 'opacity 0.5s ease';
      preloader.style.opacity = '0';
      setTimeout(function() {
        preloader.style.display = 'none';
      }, 500);
    }
  }

  window.addEventListener('load', handlePreloader);
  setTimeout(handlePreloader, 1500); // safety fallback

  document.addEventListener('DOMContentLoaded', function() {
    // 1. Mobile navigation toggle
    var openBtns = document.querySelectorAll('.mobail-menu .navbar-toggler, .open-btn');
    var closeBtns = document.querySelectorAll('.menu-close');
    var navHolders = document.querySelectorAll('.navigation-holder');

    openBtns.forEach(function(btn) {
      btn.addEventListener('click', function(e) {
        e.preventDefault();
        navHolders.forEach(function(nh) {
          nh.classList.toggle('slideInn');
        });
      });
    });

    closeBtns.forEach(function(btn) {
      btn.addEventListener('click', function(e) {
        e.preventDefault();
        navHolders.forEach(function(nh) {
          nh.classList.remove('slideInn');
        });
      });
    });

    // 2. Mobile sub-menu toggle
    var menuItemsWithChildren = document.querySelectorAll('.menu-item-has-children > a');
    menuItemsWithChildren.forEach(function(link) {
      link.addEventListener('click', function(e) {
        if (window.innerWidth <= 991) {
          var subMenu = link.nextElementSibling;
          if (subMenu && subMenu.classList.contains('sub-menu')) {
            e.preventDefault();
            var isOpen = subMenu.style.display === 'block';
            // close siblings
            var parent = link.parentElement;
            if (parent && parent.parentElement) {
              var siblingSubs = parent.parentElement.querySelectorAll('.sub-menu');
              siblingSubs.forEach(function(s) {
                if (s !== subMenu) s.style.display = 'none';
              });
            }
            subMenu.style.display = isOpen ? 'none' : 'block';
          }
        }
      });
    });

    // 3. Mini Cart slide-out
    var cartToggles = document.querySelectorAll('.cart-toggle-btn');
    var cartCloses = document.querySelectorAll('.mini-cart-close');
    var miniCartPanels = document.querySelectorAll('.mini-cart-content');

    cartToggles.forEach(function(btn) {
      btn.addEventListener('click', function(e) {
        e.preventDefault();
        e.stopPropagation();
        miniCartPanels.forEach(function(panel) {
          panel.classList.toggle('mini-cart-content-toggle');
        });
      });
    });

    cartCloses.forEach(function(btn) {
      btn.addEventListener('click', function(e) {
        e.preventDefault();
        miniCartPanels.forEach(function(panel) {
          panel.classList.remove('mini-cart-content-toggle');
        });
      });
    });

    // Remove cart item click handler
    var deleteBtns = document.querySelectorAll('.mini-cart-item-des .del-icon, .mini-cart-item-close');
    deleteBtns.forEach(function(btn) {
      btn.addEventListener('click', function(e) {
        e.preventDefault();
        var item = btn.closest('.mini-cart-item');
        if (item) {
          item.remove();
          var countEls = document.querySelectorAll('.cart-count');
          var current = parseInt(countEls[0] ? countEls[0].textContent : '0') || 0;
          var next = Math.max(0, current - 1);
          countEls.forEach(function(c) { c.textContent = next; });
        }
      });
    });

    // 4. Header search form toggle
    var searchToggles = document.querySelectorAll('.search-toggle-btn');
    var searchForms = document.querySelectorAll('.header-search-form');

    searchToggles.forEach(function(btn) {
      btn.addEventListener('click', function(e) {
        e.preventDefault();
        e.stopPropagation();
        searchForms.forEach(function(form) {
          form.classList.toggle('header-search-content-toggle');
        });
      });
    });

    // Close popups when clicking outside
    document.addEventListener('click', function(e) {
      if (!e.target.closest('.mini-cart') && !e.target.closest('.mini-cart-content')) {
        miniCartPanels.forEach(function(panel) {
          panel.classList.remove('mini-cart-content-toggle');
        });
      }
      if (!e.target.closest('.header-search-form-wrapper')) {
        searchForms.forEach(function(form) {
          form.classList.remove('header-search-content-toggle');
        });
      }
    });

    // 5. Sticky header and Back to top
    var stickyHeader = document.querySelector('.navigation.sticky-header');
    var backToTop = document.querySelector('.back-to-top');

    function onScroll() {
      var scrollY = window.pageYOffset || document.documentElement.scrollTop;
      if (stickyHeader) {
        if (scrollY > 300) {
          stickyHeader.classList.add('sticky-on');
        } else {
          stickyHeader.classList.remove('sticky-on');
        }
      }
      if (backToTop) {
        if (scrollY > 300) {
          backToTop.style.display = 'block';
        } else {
          backToTop.style.display = 'none';
        }
      }
    }

    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();

    if (backToTop) {
      backToTop.addEventListener('click', function(e) {
        e.preventDefault();
        window.scrollTo({ top: 0, behavior: 'smooth' });
      });
    }

    // 6. Tab switching for event details / service details
    var tabLinks = document.querySelectorAll('.wpo-event-details-tab .nav li a, .nav-tabs .nav-link');
    tabLinks.forEach(function(link) {
      link.addEventListener('click', function(e) {
        var targetId = link.getAttribute('href');
        if (targetId && targetId.startsWith('#') && targetId.length > 1) {
          e.preventDefault();
          var container = link.closest('.wpo-event-details-wrap, .tab-wrapper') || document;
          container.querySelectorAll('.nav li a, .nav-link').forEach(function(l) { l.classList.remove('active'); });
          link.classList.add('active');
          var targetContent = document.querySelector(targetId);
          if (targetContent && targetContent.parentElement) {
            targetContent.parentElement.querySelectorAll('.tab-pane').forEach(function(pane) {
              pane.classList.remove('active', 'show');
            });
            targetContent.classList.add('active', 'show');
          }
        }
      });
    });

    // 7. Interactive donation amount buttons
    var amountButtons = document.querySelectorAll('.wpo-donate-header ul li, .give-donation-amount li');
    amountButtons.forEach(function(li) {
      li.addEventListener('click', function() {
        amountButtons.forEach(function(item) { item.classList.remove('active'); });
        li.classList.add('active');
        var customInput = document.querySelector('.custom-amount input, #custom-amount');
        if (customInput) {
          var val = li.getAttribute('data-amount') || li.textContent.replace(/[^0-9.]/g, '');
          if (val) customInput.value = val;
        }
      });
    });

  });
})(window.jQuery);
