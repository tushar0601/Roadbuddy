"use client";

import { useCallback, useEffect, useRef } from "react";
import type { Notification } from "@/lib/types";
import { apiJson } from "@/lib/api";

type Options = {
  enabled: boolean;
  intervalMs?: number;
  onData: (items: Notification[]) => void;
  onError?: (err: unknown) => void;
};

export function useNotificationsPolling({
  enabled,
  intervalMs = 12000,
  onData,
  onError,
}: Options) {
  const inFlight = useRef(false);

  const tick = useCallback(async () => {
    if (!enabled) return;
    if (document.visibilityState !== "visible") return;
    if (inFlight.current) return;

    inFlight.current = true;
    try {
      const data = await apiJson<Notification[]>("/notification/me");
      onData(data);
    } catch (e) {
      onError?.(e);
    } finally {
      inFlight.current = false;
    }
  }, [enabled, onData, onError]);

  useEffect(() => {
    if (!enabled) return;

    const id = window.setInterval(tick, intervalMs);

    const onVis = () => tick();
    document.addEventListener("visibilitychange", onVis);

    return () => {
      window.clearInterval(id);
      document.removeEventListener("visibilitychange", onVis);
    };
  }, [enabled, intervalMs, tick]);

  // Expose a manual first fetch by calling tick from the component once if you want
  return { tick };
}