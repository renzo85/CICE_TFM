const createCV = async() => {
    const res = await fetch("http://127.0.0.1:5000/cv");
    console.log(res);
};