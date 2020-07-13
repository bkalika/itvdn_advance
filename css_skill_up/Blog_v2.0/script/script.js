
//poupup
let modalBtn = document.querySelectorAll('#open__modal'),
    modal = document.querySelector('.poupup'),
    closeBtn = document.querySelectorAll('.close');

console.log(closeBtn);


function openModal (modalID) {
  modalID.classList.add('show');
  modalID.classList.remove('hide');
}

modalBtn.forEach(function(btn) {
  
  btn.addEventListener('click', function(e) {
    if (e.target == btn) {
      console.log(e.target)
      openModal (modal);
    }
  })
})

function closeModal (modalID) {
  modalID.classList.add('hide');
  modalID.classList.remove('show');
}
for (let i =0; i < closeBtn.length; i++) {
closeBtn[i].addEventListener('click', function(e) {
  if (e.target == closeBtn[i]) {
    closeModal(modal);
    
  }
})
};

modal.addEventListener('click', function(e) {
  if (e.target == modal) {
    closeModal(modal);
  }
})

// scroll


// let modalSubscribe = document.querySelector('.subscribe');

// window.addEventListener('scroll', function () {
//   let scrollPosition = +pageYOffset,
//   poupupInitiationPosition = +Math.round(document.documentElement.scrollHeight / 2),
//   divergens = scrollPosition - poupupInitiationPosition;
//   document.getElementById('scrollPosition').innerHTML = 'scroll pos ' + scrollPosition;
//   document.getElementById('initPos').innerHTML = 'poup init ' + poupupInitiationPosition;
//   if ( scrollPosition === poupupInitiationPosition) {
//     openModal(modalSubscribe);
//   }
//   if ((divergens > -5) && (divergens < 5)) {
//     openModal(modalSubscribe);
//   }
// });

// console.log('modalSubscribe =' + modalSubscribe);

// for (let i =0; i < closeBtn.length; i++) {
//   closeBtn[i].addEventListener('click', function(e) {
//     if (e.target == closeBtn[i]) {
//       closeModal(modalSubscribe);
      
//     }
//   })
//   };

//   modalSubscribe.addEventListener('click', function(e) {
//   if (e.target == modalSubscribe) {
//     closeModal(modalSubscribe);
//   }
// })


// mobile menu
let mobileMenu = document.querySelector('.nav-mobile-menu'),
    mainMenu = document.querySelector('.navigation');

    mobileMenu.addEventListener('click', function() {
      mobileMenu.classList.toggle('active-menu')
      if (mobileMenu.classList.contains('active-menu')) {
        mainMenu.classList.add('active-menu')
      }else {
        mainMenu.classList.remove('active-menu')
      }
    })

// lesson 24
$('#nav').onePageNav ({
  currentClass: 'current'
})
