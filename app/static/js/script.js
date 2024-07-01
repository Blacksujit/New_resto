const accessKey = 'ia2QD4gbCmduLNoWSLvlO5jfos1fG1fpBp3zNxHjcuw';

const fetchImage = async () => {
  try {
    const response = await fetch(`https://api.unsplash.com/photos/random?client_id=${accessKey}`);
    const data = await response.json();
    
    const imageContainer = document.getElementById('image-container');
    const imgElement = document.createElement('img');
    imgElement.src = data.urls.small;
    imgElement.alt = data.alt_description;
    
    imageContainer.appendChild(imgElement);
  } catch (error) {
    console.error('Error fetching image from Unsplash:', error);
  }
};

document.addEventListener('DOMContentLoaded', fetchImage);
