/**
* PHP Email Form Validation - v3.5
* URL: https://bootstrapmade.com/php-email-form/
* Author: BootstrapMade.com
*/
(function () {
  "use strict";

  let forms = document.querySelectorAll('.php-email-form');

  forms.forEach( function(e) {
    e.addEventListener('submit', function(event) {
      event.preventDefault();

      let thisForm = this;

      let action = thisForm.getAttribute('action');
      let recaptcha = thisForm.getAttribute('data-recaptcha-site-key');
      
      if( ! action ) {
        displayError(thisForm, 'The form action property is not set!')
        return;
      }
      thisForm.querySelector('.loading').classList.add('d-block');
      thisForm.querySelector('.error-message').classList.remove('d-block');
      thisForm.querySelector('.sent-message').classList.remove('d-block');

      let formData = new FormData( thisForm );

      if ( recaptcha ) {
        if(typeof grecaptcha !== "undefined" ) {
          grecaptcha.ready(function() {
            try {
              grecaptcha.execute(recaptcha, {action: 'php_email_form_submit'})
              .then(token => {
                formData.set('recaptcha-response', token);
                php_email_form_submit(thisForm, action, formData);
              })
            } catch(error) {
              displayError(thisForm, error)
            }
          });
        } else {
          displayError(thisForm, 'The reCaptcha javascript API url is not loaded!')
        }
      } else {
        php_email_form_submit(thisForm, action, formData);
      }
    });
  });

  function php_email_form_submit(thisForm, action, formData) {
    fetch(action, {
      method: 'POST',
      body: formData,
      headers: {'X-Requested-With': 'XMLHttpRequest'}
    })
    .then(response => {
      if (!response.ok) {
        return response.text().then(text => {
          throw new Error(text || ('Form submission failed with status ' + response.status + ' from: ' + action));
        });
      }
      return response.text();
    })
    .then(data => {
      thisForm.querySelector('.loading').classList.remove('d-block');
      // Support original 'OK' (php template) or any 2xx response (e.g. FormSubmit / Formspree)
      const isSuccess = true; // already passed response.ok check
      if (isSuccess) {
        thisForm.querySelector('.sent-message').classList.add('d-block');
        thisForm.reset(); 
      } else {
        throw new Error(data ? data : 'Form submission failed and no error message returned from: ' + action); 
      }
    })
    .catch((error) => {
      displayError(thisForm, error);
    });
  }

  function displayError(thisForm, error) {
    thisForm.querySelector('.loading').classList.remove('d-block');
    
    let msg = error;
    if (error instanceof Error) {
      msg = error.message || error.toString();
    }
    
    // Make Formspree / service errors user-friendly instead of raw JSON
    const lower = (msg || '').toLowerCase();
    if (lower.includes('form not found') || lower.includes('form_not_found')) {
      msg = 'Contact service is not configured yet. Please email me directly at deepakv.knit@gmail.com';
    } else if (lower.includes('{"error"') || lower.includes('form not found')) {
      msg = 'Submission service error. Please try again later or contact me directly.';
    }
    
    thisForm.querySelector('.error-message').innerHTML = msg;
    thisForm.querySelector('.error-message').classList.add('d-block');
  }

})();