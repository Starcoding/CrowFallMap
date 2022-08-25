<template>
  <v-app app>
    <v-navigation-drawer permanent app>
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="text-h6">
            CrowfallMap
          </v-list-item-title>
          <v-list-item-subtitle>
            Enjoy
          </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>

      <v-list dense nav>
        <v-list-item-group v-model="selectedMap" color="primary">
          <v-list-item v-for="map in mapList" :key="map.id" link :to="{ name: 'map', params: { id: map.id } }">
            <v-list-item-icon>
              <v-icon>{{ locationTypesIcons[map.type_of_location] }}</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title>{{ map.location_name }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>

      <template v-slot:append>
        <div class="pa-2">
          <v-btn color="primary" block @click.stop="isShowCreateMapDialog = true">
            Добавить карту
          </v-btn>
        </div>
      </template>
    </v-navigation-drawer>
    <v-main app class="main">
      <v-container ca fill-height class="container d-flex">
        <keep-alive>
          <router-view v-bind:key="$route.fullPath" @dot="handleStartCreateDot"></router-view>
        </keep-alive>
      </v-container>
    </v-main>
    <v-footer app>
      AppVersion {{ version }}
    </v-footer>
    <template>
      <CreateMapDialog :show="isShowCreateMapDialog" @save="handleSaveCreateMap"
        @cancel="isShowCreateMapDialog = false" />
      <CreateDotDialog :show="isShowCreateDotDialog" @save="handleSaveCreateDot" @cancel="handleCancelCreateDot" />
    </template>
  </v-app>
</template>

<script>
import CreateMapDialog from './components/CreateMapDialog.vue';
import { getMapList, createMap } from './services';
import { LOCATION_TYPES_ICONS } from './config';
import { version } from '../package.json';
import CreateDotDialog from './components/CreateDotDialog.vue';

export default {
  name: 'App',

  components: {
    CreateMapDialog,
    CreateDotDialog
  },

  data() {
    return {
      version,
      locationTypesIcons: LOCATION_TYPES_ICONS,
      mapList: [],
      selectedMap: null,
      isShowCreateMapDialog: false,
      isShowCreateDotDialog: false,
      dotData: null,
    }
  },

  async created() {
    await this.updateMaps();
  },

  methods: {
    async updateMaps() {
      this.mapList = await getMapList();
    },

    async createMap(mapData) {
      try {
        const result = await createMap(mapData);
        this.mapList.push(result);
      } catch (e) {
        console.error(e);
      }
    },

    async handleSaveCreateMap(mapData) {
      await this.createMap(mapData);
      this.isShowCreateMapDialog = false;
    },

    handleStartCreateDot(data) {
      this.dotData = data;
      this.isShowCreateDotDialog = true;
    },

    handleSaveCreateDot(data) {
      this.dotData = {...this.dotData, ...data};
    },

    handleCancelCreateDot() {
      this.isShowCreateDotDialog = false;
      this.dotData = null;
    }
  }
}
</script>

<style scoped>
.main {
  height: 100vh;
}

.container {
  max-width: 100%;
}
</style>
