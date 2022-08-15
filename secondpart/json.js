const validJSON = obj => {
    try {
      JSON.parse(obj);
      return true;
    } catch (e) {
      return false;
    }
  };
  console.log(validJSON('{"name":"Binod Tamang","College": "ISMT"}'));
  