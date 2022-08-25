<template>
  <v-dialog :value="show" transition="dialog-top-transition" max-width="600">
    <v-card>
      <v-toolbar color="primary" dark>Добавление карты</v-toolbar>
      <v-card-text class="pt-8">
        <v-form ref="form" v-model="valid">
          <v-container>
            <v-row>
              <v-col>
                <v-file-input v-model="image" :rules="imageRules" label="Скриншот карты" filled
                  prepend-icon="mdi-panorama-variant-outline" />
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-text-field v-model="name" :rules="nameRules" label="Название карты" placeholder="Название карты"
                  filled />
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-select :items="locationTypes" v-model="type" item-text="text" item-value="value" filled
                  label="Тип карты" />
              </v-col>
            </v-row>
          </v-container>
        </v-form>
      </v-card-text>
      <v-card-actions class="justify-end">
        <v-btn color="primary" :disabled="isLoading" @click="handleSaveCreateMapDialog">
          Сохранить
        </v-btn>
        <v-btn text @click="handleCloseCreateMapDialog">
          Закрыть
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import { LOCATION_TYPES } from '../config';

export default {
  name: 'CreateMapDialog',

  props: {
    show: {
      type: Boolean,
      required: true,
    }
  },

  data() {
    return {
      valid: true,
      locationTypes: LOCATION_TYPES,
      type: 'adventure',
      name: '',
      nameRules: [
        v => !!v || 'Укажите название'
      ],
      image: null,
      imageRules: [
        v => !!v || 'Добавьте изображение'
      ],
      isLoading: false,
    }
  },

  methods: {
    validate() {
      this.$refs.form.validate();
    },

    async handleSaveCreateMapDialog() {
      const { valid, image, type, name } = this;
      this.validate();
      if (!valid) return;

      this.isLoading = true;
      this.$emit('save', { image, type, name });
    },

    handleCloseCreateMapDialog() {
      this.$refs.form.reset();
      this.type = 'adventure';
      this.$emit('cancel');
    }
  }
}
</script>
