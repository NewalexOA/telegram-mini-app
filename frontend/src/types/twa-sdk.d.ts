declare module '@twa-dev/sdk' {
  export const WebApp: {
    ready: () => void;
    initData: string;
    initDataUnsafe: {
      user: {
        id: number;
        first_name: string;
        last_name?: string;
        username?: string;
        language_code?: string;
        is_premium?: boolean;
      };
    };
    sendData: (data: string) => void;
    close: () => void;
  };
} 