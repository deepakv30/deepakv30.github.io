// Simple Service Worker for PWA offline support (Phase 3)
// Caches core assets for a more app-like experience on repeat visits.
// Note: GitHub Pages works well with this; update cache name on changes.

const CACHE_NAME = 'deepakv-portfolio-v1';
const ASSETS_TO_CACHE = [
  '/',
  '/index.html',
  '/assets/css/style.css',
  '/assets/js/main.js',
  '/manifest.json',
  '/assets/vendor/bootstrap/css/bootstrap.min.css',
  '/assets/vendor/bootstrap-icons/bootstrap-icons.css',
  '/assets/vendor/typed.js/typed.min.js',
  '/assets/vendor/bootstrap/js/bootstrap.bundle.min.js',
  '/assets/vendor/php-email-form/validate.js',
  '/assets/img/mypic-removebg-preview.webp',
  '/assets/img/hero-bg.webp',
  '/assets/img/overlay-bg.webp',
  '/assets/img/Todo-Application.webp',
  '/assets/img/hero-bg2.webp',
  // Add more images or pages (blog) as needed for fuller offline
];

// Install: cache core assets
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => {
        console.log('[SW] Caching core assets');
        return cache.addAll(ASSETS_TO_CACHE);
      })
      .then(() => self.skipWaiting())
  );
});

// Activate: clean old caches
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames
          .filter((name) => name !== CACHE_NAME)
          .map((name) => caches.delete(name))
      );
    }).then(() => self.clients.claim())
  );
});

// Fetch: serve from cache, fallback to network
self.addEventListener('fetch', (event) => {
  if (event.request.method !== 'GET') return;

  event.respondWith(
    caches.match(event.request)
      .then((cachedResponse) => {
        if (cachedResponse) {
          return cachedResponse;
        }
        return fetch(event.request).then((response) => {
          // Optionally cache new successful responses (e.g. images)
          if (response && response.status === 200 && response.type === 'basic') {
            const responseToCache = response.clone();
            caches.open(CACHE_NAME).then((cache) => {
              cache.put(event.request, responseToCache);
            });
          }
          return response;
        }).catch(() => {
          // Offline fallback for HTML (could serve cached index)
          if (event.request.destination === 'document') {
            return caches.match('/index.html');
          }
        });
      })
  );
});
