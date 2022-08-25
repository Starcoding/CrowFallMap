export async function getMapList() {
  const url = '/maps/';

  const responce = await fetch(url, {
    method: 'GET'
  });

  return responce.json();
}

export async function getMap(id) {
  const url = `/maps/${id}/`;

  const responce = await fetch(url, {
    method: 'GET'
  });

  return responce.json();
}

export async function createMap({ image, name, type }) {
  const url = '/maps/';
  const formData = new FormData();

  formData.append('image', image);
  formData.append('location_name', name);
  formData.append('type_of_location', type);

  const responce = await fetch(url, {
    method: 'POST',
    body: formData
  });

  return responce.json();
}

export default {
  getMapList,
  createMap
};
