// ... (scene, camera, renderer, controls, lights comme avant)

const textureLoader = new THREE.TextureLoader();
const satelliteTexture = textureLoader.load('https://www.solarviews.com/raw/africa/africa.jpg'); // Texture Afrique (zoom sur Gabon) – remplace par meilleure high-res Gabon
const displacementMap = textureLoader.load('https://example.com/gabon-heightmap.jpg'); // Télécharge une heightmap gratuite (ex. de NASA SRTM)

// Charger GEOJSON provinces (téléchargé dans static/data/gabon_provinces.geojson)
fetch('/static/data/gabon_provinces.geojson')
    .then(res => res.json())
    .then(geojson => {
        geojson.features.forEach(feature => {
            const provinceName = feature.properties.name || feature.properties.ADM1_FR; // Adaptez selon le GEOJSON
            const coords = feature.geometry.coordinates;

            // Parser coords (simplifié pour MultiPolygon/Polygon)
            const shapes = [];
            coords.forEach(poly => {
                poly.forEach(ring => {
                    const shape = new THREE.Shape();
                    ring.forEach((point, i) => {
                        const x = (point[0] - 11.5) * 10; // Scale/center Gabon (lon 8.5-14.5)
                        const y = (point[1] - 0) * 10;   // lat -4 à 2
                        if (i === 0) shape.moveTo(x, y);
                        else shape.lineTo(x, y);
                    });
                    shapes.push(shape);
                });
            });

            shapes.forEach(shape => {
                const extrudeSettings = { depth: 3 + Math.random() * 2, bevelEnabled: true, bevelSize: 0.5 };
                const geometry = new THREE.ExtrudeGeometry(shape, extrudeSettings);
                const material = new THREE.MeshStandardMaterial({
                    map: satelliteTexture,
                    displacementMap: displacementMap,
                    displacementScale: 1.5, // Relief réaliste
                    metalness: 0.2,
                    roughness: 0.8
                });
                const mesh = new THREE.Mesh(geometry, material);
                mesh.userData.province = provinceName;
                mesh.position.z = -1; // Légère profondeur
                scene.add(mesh);

                // Glow survol
                mesh.onMouseOver = () => {
                    mesh.material.emissive = new THREE.Color(0x00ff9d);
                    mesh.material.emissiveIntensity = 0.8;
                };
                mesh.onMouseOut = () => {
                    mesh.material.emissive = new THREE.Color(0x000000);
                };
            });
        });
    });

// Raycaster survol/clic comme avant, mais avec fetch API pour infos exactes
// ... (code onMouseMove/onClick mis à jour pour utiliser userData.province)

// Parcours biodiversité immersif
document.getElementById('start-tour').addEventListener('click', () => {
    // Ex. Loango : Caméra fly-through
    new TWEEN.Tween(camera.position)
        .to({ x: 20, y: 10, z: 15 }, 8000)
        .easing(TWEEN.Easing.Cubic.InOut)
        .start();

    // Ajoute gorille GLTF (télécharge gratuit Sketchfab : gorilla.glb)
    const gltfLoader = new THREE.GLTFLoader();
    gltfLoader.load('https://example.com/gorilla.glb', (gltf) => {
        const gorilla = gltf.scene;
        gorilla.scale.set(2,2,2);
        scene.add(gorilla);
        function lookAtCamera() {
            gorilla.lookAt(camera.position);
            requestAnimationFrame(lookAtCamera);
        }
        lookAtCamera();
    });

    // Particules pluie/forêt
    const particlesGeo = new THREE.BufferGeometry();
    const particlesCount = 5000;
    const posArray = new Float32Array(particlesCount * 3);
    for(let i = 0; i < particlesCount * 3; i++) posArray[i] = (Math.random() - 0.5) * 50;
    particlesGeo.setAttribute('position', new THREE.BufferAttribute(posArray, 3));
    const particlesMat = new THREE.PointsMaterial({ color: 0x88ff88, size: 0.05, transparent: true });
    const particles = new THREE.Points(particlesGeo, particlesMat);
    scene.add(particles);

    // Animation pluie
    function rain() {
        particles.position.y -= 0.1;
        if (particles.position.y < -20) particles.position.y = 20;
        requestAnimationFrame(rain);
    }
    rain();
});

// Océan simple (plane avec wave shader)
const oceanGeo = new THREE.PlaneGeometry(100, 100);
const oceanMat = new THREE.MeshStandardMaterial({ color: 0x006994, roughness: 0.8 });
const ocean = new THREE.Mesh(oceanGeo, oceanMat);
ocean.rotation.x = -Math.PI / 2;
ocean.position.y = -2;
scene.add(ocean);

// Animate loop avec TWEEN.update()