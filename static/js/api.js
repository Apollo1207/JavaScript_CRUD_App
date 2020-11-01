const BASE_URL = "http://localhost:3000/api";
const RESOURSE_URL = `${BASE_URL}/sportBuild`;

const baseRequest = async ({ urlPath = "", method = "GET", body = null }) => {
  try {
    const reqParams = {
      method,
      headers: {
        "Content-Type": "application/json",
      },
    };

    if (body) {
      reqParams.body = JSON.stringify(body);
    }

    return await fetch(`${RESOURSE_URL}${urlPath}`, reqParams);
  } catch (error) {
    console.error("HTTP ERROR: ", error);
  }
};

export const getAllSportBuilds = async () => {
  const rawResponse = await baseRequest({ method: "GET" });

  return await rawResponse.json();
};

export const createSportBuild = (body) => baseRequest({ method: "POST", body });

export const updateSportBuild = (id, body) =>
  baseRequest({ urlPath: `/${id}`, method: "PATCH", body });

export const deleteSportBuild = (id) =>
  baseRequest({ urlPath: `/${id}`, method: "DELETE" });
