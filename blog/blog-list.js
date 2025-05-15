// blog-list.js
// List of blog posts (add new posts here)
const blogs = [
  {
    title: "Linux Commands Cheat-sheet",
    description: "This article will help us with all the very basic commands in Linux for working with files and directories. I have run all commands on a Linux machine running on AWS...",
    category: "Linux",
    author: "Deepak Vishwakarma",
    time: "10 min",
    image: "https://miro.medium.com/max/1100/0*tk0BvANKXfP85bV0",
    url: "linux-commands-cheat-sheet.html"
  },
  {
    title: "Getting started with Shell Scripting",
    description: "Here, we will try to cover basic terminologies used in shell scripting and will try to get a bigger picture of what shell scripting is not. We will try to bust the myth...",
    category: "Shell Scripting",
    author: "Deepak Vishwakarma",
    time: "10 min",
    image: "https://miro.medium.com/max/1100/1*I0oi-OIRmQOHCK_1G8ahhQ.webp",
    url: "getting-started-with-shell-scripting.html"
  },
  {
    title: "Kick-start your AWS Cloud journey within 10 minutes",
    description: "This article will help you to kick-start your AWS cloud journey by knowing about the basics and being familiar with the jargon used in AWS. What Is Cloud Computing? Cloud computing is the on-demand delivery...",
    category: "Amazon Web Services",
    author: "Deepak Vishwakarma",
    time: "10 min",
    image: "https://miro.medium.com/max/1100/1*Hk7uuC6HfPwTd9nMws81Ww.webp",
    url: "kick-start-aws-cloud-journey.html"
  }
];

const blogList = document.getElementById('blog-list');
if (blogList) {
  blogs.forEach(blog => {
    const col = document.createElement('div');
    col.className = 'col-md-4';
    col.innerHTML = `
      <div class="card card-blog">
        <div class="card-img">
          <a href="${blog.url}"><img src="${blog.image}" alt="" class="img-fluid"></a>
        </div>
        <div class="card-body">
          <div class="card-category-box">
            <div class="card-category">
              <h6 class="category">${blog.category}</h6>
            </div>
          </div>
          <h3 class="card-title"><a href="${blog.url}">${blog.title}</a></h3>
          <p class="card-description">${blog.description}</p>
        </div>
        <div class="card-footer">
          <div class="post-author">
            <a href="#">
              <img src="../assets/img/mypic.jpg" alt="" class="avatar rounded-circle">
              <span class="author">${blog.author}</span>
            </a>
          </div>
          <div class="post-date">
            <span class="bi bi-clock"></span> ${blog.time}
          </div>
        </div>
      </div>
    `;
    blogList.appendChild(col);
  });
}
