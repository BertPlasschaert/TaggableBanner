![banner](banner833743.svg)

Try it out on [my profile](https://github.com/BertPlasschaert), or [read about the journey building it.](/writeup/writeup.md)

<details>

<summary>Users who have tagged the banner</summary>

<!--begin usernames-->
###### [BertPlasschaert](https://github.com/BertPlasschaert) on 18/01/2026
<!--end usernames-->

##### Thank you all for adding your username!

</details>

# Taggable Banner

By implementing this system you can let visitors add their usernames to the repo banner.
Inspired by the way [timburgan](https://github.com/timburgan) creatively used github actions
to update his chess README.md. I wanted to pimp my own homepage by creating some kind of
guestbook. Give it a try [here](https://github.com/BertPlasschaert)!

## How does it work?

By clicking the link under the banner you will be prompted to submit a pre-filled issue, triggering a Github action.
This action will run the python code from this repo and execute the following steps:
- Check the `README.MD` file which doubles as a registry for existing tags.
  - If the tag already exists, add a comment to the issue and close it.
- Add the username to the `README.MD` file and add the tag to the `banner.svg`.
- Update the `banner.svg` filename with a timestamp to invalidate the Github caching system.
- Close the issue and add a reply, prompting the user to check it out.

The banner SVG file scales perfectly for every screen, and is **light and dark mode** compatible!
| ![banner_dark](examples/banner_example_dark.svg)| ![banner_light](examples/banner_example_light.svg)|
| -------- | ------- |
| $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ Dark mode $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$| $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ Light mode $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$|

## Test it locally


If you want to test the functionality on your own machine you can pip install the repo using the following command:  
`pip install git+https://github.com/BertPlasschaert/TaggableBanner`

This provides three CLI commands:
- A check to see if the username tag is already in the banner: `taggablebanner check "<username>"`
- A command to add the username tag to the banner: `taggablebanner add "<username>"`
- A command to rename the banner SVG file to a random name: `taggablebanner fix_cache`
  > This ensures that the file pointer in the README.md file can never be cached, updates will show up instantly.


## Add it to your own repo
Start by copying the [workflow file](.github/workflows/add_username.yml) into your own repo.

You will have to set the following settings in your repository settings:
- **issues** are **enabled**, 
- **actions** have **read and write permissions**

You can either copy the [README_example.md](examples/README_example.md) file to start from.
Or copy the `begin` and `end usernames` markers from it, and paste it into your existing README.md file.  
Don't forget to update the link in the button pointing towards your own repo.
The URL params in that link will prepopulate the issue body and title, so be careful updating it.

## Customize it

I suggest you read [the writeup](/writeup/writeup.md) first.  

The title: `Hello!` is a string value which you can easily update.
Only the bricks, cracks and splats are file SVG elements, which require more work to update.
The bulk of your work will be to update the 'magic numbers' that position these elements.
I've implemented exclusion zones around the brick elements and title, no tags can spawn fully over them.
So if you change these elements, make sure to update them accordingly.
Adding fonts is possible but you'll need to [encode them](https://blog.frankel.ch/fonts-embedded-svg/) and create configs.

## Attributions

- [Tim Burgan](https://github.com/timburgan/timburgan) for the creative use of github actions and sparking this idea.
- [Nicolas Fränkel](https://blog.frankel.ch/fonts-embedded-svg/) for his article on SVG font embeddings.
- [orsinium](https://github.com/orsinium-labs/svg.py) for creating an SVG interface python module and making my life a lot easier.
- [Dafont](https://www.dafont.com/crysh-graffiti.font):
  - fitrahtype - [crysh graffiti](https://www.dafont.com/crysh-graffiti.font)
  - Woodcutter - [graffiti city](https://www.dafont.com/graffiti-city.font)
  - Nirmana Visual - [graffiti youth](https://www.dafont.com/graffiti-youth.font)
  - Rissyletter Studio - [shock graffiti](https://www.dafont.com/shock-graffiti.font)
- [The Noun Project](https://www.dafont.com/crysh-graffiti.font):
  - Bombasticon Studio - [Brick wall](https://thenounproject.com/browse/creator/bombasticon/search/?avatarUrl=https%3A%2F%2Fstatic.thenounproject.com%2Favatars%2F4446273%2Fresized%2F260%2F260%2F2f3bb0577086a6d33e37929f7c3b2139.png&name=Bombasticon%20Studio&p=1&q=brick)
  - Sean Maldjian - [Wall cracks](https://thenounproject.com/browse/creator/sean.maldjian/search/?avatarUrl=https%3A%2F%2Fstatic.thenounproject.com%2Favatars%2F515285%2Fresized%2F260%2F260%2Fjefre_cantu-ledesma-Love.png&name=Sean%20Maldjian&p=1&q=crack)
  - Marie Van den Broeck - [Stain 01](https://thenounproject.com/icon/stain-732985/)
  - Lucas Helle - [Stain 02](https://thenounproject.com/icon/paint-stain-4215505/)

## License

This example and the code in it is licensed under the MIT License.
If you use this in your own repositories, please add a link back to this repo!

## Disclaimers

[![brainmadeicon](images/brainmade.svg)](https://brainmade.org/) - No GenAI / LLMs were used in and during the development of this repository.
