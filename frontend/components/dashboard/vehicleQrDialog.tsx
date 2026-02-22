/* eslint-disable @typescript-eslint/no-explicit-any */
"use client";

import { useEffect, useMemo, useState } from "react";
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog";
import type { Vehicle, Sticker } from "@/lib/types";
import { apiJson } from "@/lib/api";
import { QRCodeCanvas } from "qrcode.react";
import { toast } from "sonner";
import { Button } from "@/components/ui/button";

export function VehicleQrDialog({
  vehicle,
  onClose,
}: {
  vehicle: Vehicle | null;
  onClose: () => void;
}) {
  const open = !!vehicle;

  const base = process.env.NEXT_PUBLIC_WEB_BASE_URL || "http://localhost:3000";

  const [sticker, setSticker] = useState<Sticker | null>(null);
  const [loading, setLoading] = useState(false);
  const [err, setErr] = useState<string | null>(null);

  const url = useMemo(() => {
    if (!sticker) return "";
    return `${base}/s/${sticker.public_code}`;
  }, [base, sticker]);

  useEffect(() => {
    if (!vehicle || !open) return;

    let cancelled = false;

    async function createSticker() {
      setErr(null);
      setLoading(true);
      setSticker(null);

      try {
        const res = await apiJson<Sticker>(
          `/vehicles/${vehicle?.id}/stickers`,
          {
            method: "POST",
          },
        );

        if (!cancelled) setSticker(res);
      } catch (e: any) {
        const msg = e?.message || "Failed to generate QR";
        if (!cancelled) setErr(msg);
        toast.error(msg);
      } finally {
        if (!cancelled) setLoading(false);
      }
    }

    createSticker();

    return () => {
      cancelled = true;
    };
  }, [vehicle, open]);

  function handleClose() {
    setSticker(null);
    setErr(null);
    setLoading(false);
    onClose();
  }

  return (
    <Dialog open={open} onOpenChange={(o) => !o && handleClose()}>
      <DialogContent>
        <DialogHeader>
          <DialogTitle>QR for {vehicle?.label}</DialogTitle>
        </DialogHeader>

        <div className="flex flex-col items-center gap-3">
          {loading ? (
            <div className="text-sm text-muted-foreground">
              Generating secure QR...
            </div>
          ) : err ? (
            <div className="w-full space-y-3">
              <div className="text-sm text-red-600">{err}</div>
              <Button
                variant="outline"
                onClick={() => {
                  if (!vehicle) return;
                  setSticker(null);
                  setErr(null);
                  setLoading(true);
                  apiJson<Sticker>(`/vehicles/${vehicle.id}/stickers`, {
                    method: "POST",
                  })
                    .then((s) => setSticker(s))
                    .catch((e: any) => setErr(e?.message || "Failed"))
                    .finally(() => setLoading(false));
                }}
              >
                Retry
              </Button>
            </div>
          ) : sticker ? (
            <>
              <QRCodeCanvas value={url} size={220} />
              <div className="text-xs break-all text-muted-foreground">
                {url}
              </div>
              <div className="text-xs text-muted-foreground">
                Scan → opens secure notify page
              </div>
            </>
          ) : (
            <div className="text-sm text-muted-foreground">
              No sticker found.
            </div>
          )}
        </div>
      </DialogContent>
    </Dialog>
  );
}
