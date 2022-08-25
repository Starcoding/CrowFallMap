<template>
  <v-dialog :value="show" transition="dialog-top-transition" max-width="600">
    <v-card>
      <v-toolbar color="primary" dark>Добавление точки</v-toolbar>
      <v-card-text class="pt-8">
        <v-form ref="form" v-model="valid">
          <v-container>
            <v-row>
              <v-col>
                <v-text-field v-model="name" :rules="nameRules" label="Название" placeholder="Название" filled />
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-textarea v-model="description" :rules="descriptionRules" filled label="Описание"
                  placeholder="Описание" />
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-select :items="dotIconVariants" v-model="icon" item-text="text" item-value="value" filled
                  label="Иконка" />
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-color-picker v-model="color"></v-color-picker>
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
import { DOT_ICON_VARIANTS } from '@/config';

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

      dotIconVariants: DOT_ICON_VARIANTS,
      icon: '',
      iconRules: [
        v => !!v || 'Выберите иконку'
      ],

      color: '',
      colorRules: [
        v => !!v || 'Выберите цвет'
      ],

      name: '',
      nameRules: [
        v => !!v || 'Укажите название'
      ],

      description: '',
      descriptionRules: [
        v => !!v || 'Укажите описание'
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
