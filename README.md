<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<br />
<div align="center">
  <a href="https://github.com/hillswor/namaka-server">
    <img src="public/namaka-logo.svg" alt="Logo" width="100" height="100">
  </a>

<h3 align="center">Namaka</h3>

  <p align="center">
    The server side of a full-stack application that creates an API for the Next.js front end to interact and pull data from.  The API is connected to a PostgreSQL database hosted by Render.  The app enables reef tank enthusiasts to monitor crucial water parameters and interact with one another through a message board.
    <br />
    <a href="https://namaka-client.vercel.app/">View API</a>
    ·
    <a href="https://github.com/hillswor/namaka-server/issues">Report Bug</a>
    ·
    <a href="https://github.com/hillswor/namaka-server/issues">Request Feature</a>
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## About The Project

<div align="center">
    <img src="screenshots/namaka-root-img.png" alt="Screenshot of Home Page" width="400" height="300">
</div>


With Namaka, users can track and manage aspects of their saltwater aquariums. The user-friendly platform enables users to monitor various parameters crucial to maintaining a healthy aquatic environment. Each aquarium gets its dedicated dashboard, where you can log information, analyze trends, and optimize care routines.

Moreover, Namaka aims to be home to a thriving community with an interactive message board that allows users to ask questions, share experiences, offer advice, or simply engage in conversation.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

 [![Next][Next.js]][Next-url]
 [![React][React.js]][React-url]
 [![TailwindCSS][Tailwind]][Tailwind-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.js`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/basic-features/font-optimization) to automatically optimize and load Inter, a custom Google Font.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage

Once logged in, users can go to the "My Account" page to edit or delete existing aquariums.

<div align="center">
    <img src="screenshots/namaka-my-account.png" alt="Screenshot of 'My Account' page" width="400" height="300">
</div>
<br />
Clicking "View" will take the user to the aquarium page where they can view a chart of all the logged water parameters for that aquarium or log new parameters.
<br />
<br />
<div align="center">
    <img src="screenshots/namaka-aquarium-page.png" alt="Screenshot of 'Aquarium' page" width="400" height="300">
</div>
<br />
<div align="center">
    <img src="screenshots/namaka-water-parameters.png" alt="Screenshot of 'Water Parameter' page" width="400" height="300">
</div>
<br />
Users can also communicate with other users via the message board(The majority of current messages are from seed data via the Faker library so it is jibberish)
<br />
<br />
<div align="center">
    <img src="screenshots/namaka-message-board.png" alt="Screenshot of 'Message Board' page" width="400" height="300">
</div>
<br />
<div align="center">
    <img src="screenshots/namaka-comment-form.png" alt="Screenshot of comment form on 'Message Board'" width="400" height="300">
</div>
<br />
<div align="center">
    <img src="screenshots/namaka-comment-form.png" alt="Screenshot of comment form on 'Message Board'" width="400" height="300">
</div>
<br />
<div align="center">
    <img src="screenshots/namaka-comment-posted.png" alt="Screenshot of comment posted" width="400" height="300">
</div>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Roadmap

- [ ] Add ability for user to upload photo of their aquarium
- [ ] Add ability for users to follow/friend other users 
- [ ] Add ability for aquarium owner to temporarily share aquarium with follower/friend
  - [ ] Grant access to log parameters to shared follower/friend
- [ ] Change my account page to tabs
- [ ] Add search and filters to message board

See the [open issues](https://github.com/hillswor/namaka-client/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## License

Distributed under the MIT License. See `LICENSE.md` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Bruce Hillsworth - [@bhillsworth](https://twitter.com/bhillsworth) - bruce.hillsworth@gmail.com

Project Link: [https://github.com/hillswor/namaka-client](https://github.com/hillswor/namaka-client)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Acknowledgments

* [Dave Gray](https://www.youtube.com/watch?v=843nec-IvW0&t=3096s)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/hillswor/namaka-client.svg?style=for-the-badge
[contributors-url]: https://github.com/hillswor/namaka-client/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/hillswor/namaka-client.svg?style=for-the-badge
[forks-url]: https://github.com/hillswor/namaka-client/network/members
[stars-shield]: https://img.shields.io/github/stars/hillswor/namaka-client.svg?style=for-the-badge
[stars-url]: https://github.com/hillswor/namaka-client/stargazers
[issues-shield]: https://img.shields.io/github/issues/hillswor/namaka-client.svg?style=for-the-badge
[issues-url]: https://github.com/hillswor/namaka-client/issues
[license-shield]: https://img.shields.io/github/license/hillswor/namaka-client.svg?style=for-the-badge
[license-url]: https://github.com/hillswor/namaka-client/blob/master/LICENSE.md
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/bruce-hillsworth
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Tailwind]: https://img.shields.io/badge/tailwindcss-000000?style=for-the-badge&logo=tailwindcss&logoColor=61DAFB
[Tailwind-url]: https://tailwindcss.com/