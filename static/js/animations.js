(function () {
    'use strict';

    /* Scroll-reveal via Intersection Observer */
    function initScrollReveal() {
        var elements = document.querySelectorAll('.animate-on-scroll');
        if (!elements.length) return;

        if (!('IntersectionObserver' in window)) {
            elements.forEach(function (el) { el.classList.add('is-visible'); });
            return;
        }

        var observer = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('is-visible');
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

        elements.forEach(function (el) { observer.observe(el); });
    }

    /* Stagger children inside a container */
    function initStagger() {
        document.querySelectorAll('[data-stagger]').forEach(function (container) {
            var children = container.children;
            for (var i = 0; i < children.length; i++) {
                children[i].classList.add('animate-on-scroll');
                children[i].classList.add('delay-' + Math.min(i + 1, 5));
            }
        });
    }

    /* Button ripple on click */
    function initRipple() {
        document.addEventListener('click', function (e) {
            var btn = e.target.closest('.auth-btn, .main-button a, .btn-logout');
            if (!btn) return;

            var ripple = document.createElement('span');
            var rect = btn.getBoundingClientRect();
            var size = Math.max(rect.width, rect.height);

            ripple.style.cssText =
                'position:absolute;border-radius:50%;background:rgba(255,255,255,0.35);' +
                'width:' + size + 'px;height:' + size + 'px;' +
                'left:' + (e.clientX - rect.left - size / 2) + 'px;' +
                'top:' + (e.clientY - rect.top - size / 2) + 'px;' +
                'animation:btn-ripple 0.6s ease forwards;pointer-events:none;';

            btn.appendChild(ripple);
            setTimeout(function () { ripple.remove(); }, 600);
        });
    }

    document.addEventListener('DOMContentLoaded', function () {
        initStagger();
        initScrollReveal();
        initRipple();
    });
})();
