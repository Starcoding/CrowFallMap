<template>
  <div class="container">
    <div class="control">
      <v-btn color="primary" elevation="2" fab @click.stop="handleClickCreateDot">
        <v-icon>
          mdi-map-marker
        </v-icon>
      </v-btn>
      <v-btn color="primary" elevation="2" fab @click="handleClickCreateZone" :disabled="true">
        <v-icon>
          mdi-shape-square-plus
        </v-icon>
      </v-btn>
    </div>
    <canvas ref="canvas" class="canvas" />
  </div>

</template>
<script>
import { getMap } from '../services';

export default {
  name: 'MapView',

  data() {
    return {
      map: null,
      context: null,
      rect: null,
    }
  },

  async mounted() {
    this.map = await getMap(this.$route.params.id);

    const background = new Image();
    const canvas = this.$refs.canvas;
    this.context = canvas.getContext('2d');
    canvas.height = canvas.parentElement.offsetHeight;
    canvas.width = (canvas.height * 4) / 3;
    this.rect = canvas.getBoundingClientRect();

    background.src = this.map.image;
    background.onload = () => this.context.drawImage(background, 0, 0, canvas.width, canvas.height);
  },

  methods: {
    handleClickCreateDot() {
      document.body.style.cursor = 'crosshair';
      document.addEventListener('click', (event) => {
        document.body.style.cursor = 'default';

        if (event.target.tagName !== 'CANVAS') return;

        const x = ((event.offsetX * 100) / this.rect.width).toFixed(2);
        const y = ((event.offsetY * 100) / this.rect.height).toFixed(2);

        this.$emit('dot', {id: this.$route.params.id, x, y});
      }, { once: true })
    },

    handleClickCreateZone() {
    }
  }
}
</script>

<style scoped>
.container {
  width: 100%;
  height: 100%;
  padding: 0;
  position: relative;
  display: flex;
  justify-content: center;
}

.control {
  position: absolute;
  left: 0;
  top: 0;
  display: flex;
  gap: 16px;
  flex-direction: column;
}
</style>